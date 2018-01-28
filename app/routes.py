from app import app
from flask import render_template, session

@app.route('/')
@app.route('/index')
def index():
    if 'user' not in session:
        return render_template('index.html.tpl')
    else:
        return main(session['user'])

@app.route('/login/<user>')
def login(user):
    session['user'] = user
    return main()

@app.route("/main")
def main():
    user = session['user']
    online_users = []
    return render_template('main.html.tpl', user=user, online_users=online_users)

@app.route('/game')
def game(session, user, role, level):
    return render_template('game.html.tpl', role=role, user=user, level=level)
