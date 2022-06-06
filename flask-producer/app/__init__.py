from flask import Flask
# from .config import Config
# from flask_mongoengine import MongoEngine
from celery import Celery

app = Flask(__name__)
cel_app = Celery('tasks',
                 broker='amqp://user:pass@rabbit:5672',
                 backend='mongodb://mongodb:27017/backdb')
# app.config.from_object(Config)

# db = MongoEngine()
# db.init_app(app)

from . import views
