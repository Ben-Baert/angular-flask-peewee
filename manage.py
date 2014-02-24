import os
import json
import argparse
import requests

from angular_flask.core import db
from angular_flask import app, models
from angular_flask.models import *
from peewee import *
from flask.ext.script import Manager

manager = Manager(app)

@manager.command
def create_db():
	Post.create_table(fail_silently = True)

@manager.command
def drop_db():
	Post.delete_table(fail_silently = True)
	
@manager.command
def seed_db():
	with open('data/db_items.json', 'r') as f:
		seed_data = json.loads(f.read())
			
	for item_class in seed_data:
		items = seed_data[item_class]
		print items
		for item in items:
			print item
			Post.create(title = item["title"], body = item["body"], pub_date=datetime.now())

	print '\nSample data added to database!'
	
@manager.shell
def make_shell_context():
    return dict(app=app, db=db, models=models)
	
"""
	elif args.command == 'seed_db' and args.seedfile:
		with open(args.seedfile, 'r') as f:
			seed_data = json.loads(f.read())
		
		for item_class in seed_data:
			items = seed_data[item_class]
			print items
			for item in items:
				print item
				create_sample_db_entry('api/' + item_class, item)

		print '\nSample data added to database!'
	else:
		raise Exception('Invalid command')

if __name__ == '__main__':
	main()
"""

if __name__ == "__main__":
    manager.run()
