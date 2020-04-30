from resources.wine import WineView
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

api.add_resource(WineView, '/')
