from flask_restful import Resource
from resources.models import Wine
from flask import request, jsonify, make_response, g


class WineView(Resource):

    def get(self):
        try:
            wine = Wine.query.get(1)
            return make_response({'price': wine.price}, 200)
        except:
            return make_response({'error': 'world'}, 400)
