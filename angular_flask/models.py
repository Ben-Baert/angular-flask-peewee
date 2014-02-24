from datetime import datetime

from angular_flask.core import db
from angular_flask import app

class Post(db.Model):
	title = CharField()
	body = TextField()
	pub_date = DateTimeField(default = datetime.now())

# models for which we want to create API endpoints
app.config['API_MODELS'] = { 'post': Post }

# models for which we want to create CRUD-style URL endpoints,
# and pass the routing onto our AngularJS application
app.config['CRUD_URL_MODELS'] = { 'post': Post }
