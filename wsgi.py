""" This module is used by Gunicorn to start the production server. """
from app import app, db

app.config.from_object('api.config.ProductionConfig')
db.init_app(app)
