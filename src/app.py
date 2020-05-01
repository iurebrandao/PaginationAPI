from flask import Flask
from flask_restful import Resource, Api
from src.wine import WineView


app = Flask(__name__)
api = Api(app)

api.add_resource(WineView, '/wine')
