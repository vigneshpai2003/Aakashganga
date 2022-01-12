import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

if os.getenv('DEPLOYMENT'):
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
        username=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        hostname=os.getenv('DB_HOST'),
        databasename=os.getenv('DB_NAME'),
    )
    app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
else:
    app.config['SECRET_KEY'] = '12345'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"

db = SQLAlchemy(app)

from AGapp import models
from AGapp import routes