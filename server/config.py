import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

class Configure:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pizza.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(Configure)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
