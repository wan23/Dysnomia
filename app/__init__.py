from flask import Flask

app = Flask(__name__)
app.secret_key = 'A0Zr98j/sdf2R~XHH!jmN]LWX/,?RT' #sshhh

from app import routes
