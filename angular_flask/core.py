from angular_flask import app

from flask_peewee.db import Database
from flask_peewee.rest import RestAPI

db = Database(app)

api_manager = RestAPI(app)

