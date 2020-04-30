from flask_restful import Resource
from flask import request, jsonify, make_response, g
from .models import Wine
from .jsonify import wine_jsonify


class WineView(Resource):

    def get(self):
        try:
            wines = Wine.query.all()
            wines_json = [wine_jsonify(wine) for wine in wines]

            return make_response(jsonify(wines_json), 200)
        except:
            return make_response({'error': 'world'}, 400)
