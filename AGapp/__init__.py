from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "0677c9daf9cb31949f0b5555b0afc3e0"

from AGapp import routes