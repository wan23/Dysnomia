from app import app
from flask import render_template, session, redirect, url_for, request
from app.database import db, Game

@app.route('/')
@app.route('/index')
def index():
    if 'user' not in session:
        return render_template('index.html.tpl')
    else:
        return main(session['user'])

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

@app.route('/game')
def game(session, user, role, level):
    return render_template('game.html.tpl', role=role, user=user, level=level)
