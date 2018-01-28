from app import app
from flask import render_template, session, redirect, url_for, request
from app.database import db, Game

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
        if not game:
            return "ERROR: GAME NOT FOUND"
        if request.form['role'] == 'viewer':
            if not game.viewer_name:
                game.viewer_name = session['user']
                session['current_game'] = game_id
        elif request.form['role'] == 'typer':
            if not game.typer_name:
                game.typer_name = session['user']
                session['current_game'] = game_id
        else:
            return 'error: wtf'
        db.session.add(game)
        db.session.commit()
        print("New Game: " + str(game.id))
        session['current_game'] = game.id
        return redirect(url_for('main'))
    else:
        return 'ERROR'

@app.route('/game')
def game():
    if 'current_game' not in session:
        return redirect(url_for('main'))
    game = Game.query.filter(Game.id == session['current_game']).first()
    if not game:
        del session['current_game']
        return redirect(url_for('main'))
    if game.viewer_name == session['user']:
        return render_template('viewer.html.tpl', game=game)
    elif game.typer_name == session['user']:
        return render_template('typer.html.tpl', game=game)
