from angular_flask import app

from flask_peewee.db import Database
from flask.ext.restless import APIManager

db = Database(app)

api_manager = APIManager(app, flask_sqlalchemy_db=db)

