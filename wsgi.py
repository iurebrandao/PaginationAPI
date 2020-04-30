""" This module is used by Gunicorn to start the production server. """
from src.app import app
from src.models import db
from src.schema import ma

app.config.from_object('config.ProductionConfig')
db.init_app(app)
ma.init_app(app)
