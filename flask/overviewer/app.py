import os
from flask import Flask
from flask.ext.markdown import Markdown
from .models import db
from .cache import cache

app = Flask(__package__)

app.config.from_object('overviewer.settings.default')
if 'OVERVIEWER_SETTINGS' in os.environ:
    app.config.from_envvar('OVERVIEWER_SETTINGS')

db.init_app(app)
cache.init_app(app)
Markdown(app, extensions=['extra', 'toc', 'codehilite'])
