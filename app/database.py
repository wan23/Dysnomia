from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    viewer_name = db.Column(db.String(80))
    typer_name = db.Column(db.String(80))
    current_level = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<User %r>' % self.username
