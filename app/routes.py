from app import app
from flask import render_template, session, redirect, url_for, request, flash
from app.database import db, Game
from app.level import Level

@app.route('/')
@app.route('/index')
def index():
    if 'user' not in session:
        return render_template('index.html.tpl')
    else:
        return redirect(url_for('main'))

@app.route('/login', methods=['POST'])
def login():
    if request.form['user']:
        session['user'] = request.form['user']
        return redirect(url_for('main'))
    else:
        return 'ERROR'

@app.route("/main")
def main():
    user = session['user']
    games = Game.query.all()
    return render_template('main.html.tpl', user=user, games=games)

@app.route('/newgame', methods=['POST'])
def newgame():
    if 'role' in request.form:
        game = Game()
        if request.form['role'] == 'viewer':
            game.viewer_name = session['user']
        elif request.form['role'] == 'typer':
            game.typer_name = session['user']
        else:
            return 'error: wtf'
        db.session.add(game)
        db.session.commit()
        print("New Game: " + str(game.id))
        session['waiting_for_game'] = game.id
        return redirect(url_for('main'))
    else:
        return 'ERROR'

@app.route('/joingame', methods=['POST'])
def joingame():
    if 'role' in request.form and 'gameid' in request.form:
        game_id = request.form['gameid']
        game = Game.query.filter(Game.id == game_id).first()
        user = session['user']
        if not game:
            return "ERROR: GAME NOT FOUND"
        if request.form['role'] == 'viewer':
            if not game.viewer_name:
                game.viewer_name = user
        elif request.form['role'] == 'typer':
            if not game.typer_name:
                game.typer_name = user
        else:
            return 'error: wtf'
        db.session.add(game)
        db.session.commit()
        print("New Game: " + str(game.id))
        session['current_game'] = game.id
        return redirect(url_for('main'))
    else:
        return 'ERROR'

def get_current_game():
    if 'current_game' not in session:
        return None
    game = Game.query.filter(Game.id == session['current_game']).first()
    if not game:
        del session['current_game']
        return None
    return game

def get_role(user, game):
    if game.viewer_name == session['user']:
        return 'viewer'
    elif game.typer_name == session['user']:
        return 'typer'
    return None

@app.route('/game/<game_id>')
def game(game_id):
    user = session['user']

    game = Game.query.filter(Game.id == game_id).first()
    if not game:
        return redirect(url_for('main'))
    level = Level.get(game.current_level)
    role = get_role(user, game)
    if role == 'viewer':
        return render_template('viewer.html.tpl', level=level, game=game)
    elif role == 'typer':
        return render_template('typer.html.tpl', level=level, game=game)
    else:
        return redirect(url_for('main'))

@app.route('/answer', methods=["POST"])
def answer():
    if 'game_id' not in request.form or 'answer' not in request.form:
        return "Need game and answer"
    game_id = request.form['game_id']
    user = session['user']
    game = Game.query.filter(Game.id == game_id).first()
    if not game:
        return redirect(url_for('main'))
    role = get_role(user, game)
    if role != 'typer':
        return redirect(url_for('main'))
    level = Level.get(game.current_level)
    if not level:
        return "ERROR: Level not found"
    if level.answer == request.form['answer']:
        game.current_level = game.current_level + 1
        db.session.add(game)
        db.session.commit()
    else:
        flash("Sorry, but that was not the answer!")
    return redirect(url_for('game', game_id=game_id))
