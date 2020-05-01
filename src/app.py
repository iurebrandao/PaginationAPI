from flask import Flask
from flask_restful import Resource, Api
from src.wine import WineView
from flask_restful_swagger import swagger


app = Flask(__name__)
api = swagger.docs(Api(app), apiVersion='0.1')

api.add_resource(WineView, '/wine')
