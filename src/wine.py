from flask_restful import Resource
from flask import request, jsonify, make_response
from .models import Wine
from .jsonify import wine_jsonify
from config import BaseConfig
from flask_restful_swagger import swagger


class WineView(Resource):
    @swagger.operation(
        notes='Method to return the wines in a paginated way and with the desired filters',
        responseClass=Wine.__name__,
        nickname='wine',
        parameters=[
            {
                "name": "page",
                "description": "Number of the page you desire to return the rows. It must be between 1 "
                               "and the max number of pages",
                "required": True,
                "allowMultiple": False,
                "dataType": "integer",
                "paramType": "query"
            },
            {
                "name": "country",
                "description": "country you desire to return",
                "required": False,
                "allowMultiple": False,
                "dataType": "str",
                "paramType": "query"
            },
            {
                "name": "description",
                "description": "key-word of the description you desire to return",
                "required": False,
                "allowMultiple": False,
                "dataType": "str",
                "paramType": "query"
            },
            {
                "name": "points",
                "description": "wine points you desire to return",
                "required": False,
                "allowMultiple": False,
                "dataType": "integer",
                "paramType": "query"
            },
            {
                "name": "price",
                "description": "wine price you desire to return",
                "required": False,
                "allowMultiple": False,
                "dataType": "float",
                "paramType": "query"
            },
            {
                "name": "variety",
                "description": "wine variety you desire to return",
                "required": False,
                "allowMultiple": False,
                "dataType": "str",
                "paramType": "query"
            }
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "Rows with wine features in 'data' key. There is also 'has_prev_page', 'has_next_page', "
                           "'current_page', 'num_pages', 'url_next_page' keys with additional information"
            },
            {
                "code": 404,
                "message": "Invalid page number"
            },{
                "code": 400,
                "message": "Bad request"
            }
        ]
    )
    def get(self):
        """Main method to return the wine features with filters and pagination"""
        try:
            if not request.args.get('page'):
                return make_response({'page': 'this is a required param'}, 400)

            current_page = int(request.args.get('page'))

            query = Wine.query
            possible_filters = ['country', 'points', 'price', 'variety']
            filter_object = dict()

            # Getting wine filters in automate way, except for description
            for arg in request.args:
                if arg in possible_filters:
                    filter_object[arg] = request.args.get(arg)

            if request.args.get('description'):
                query = query.filter(Wine.description.contains(request.args.get('description')))

            query = query.filter_by(**filter_object)

            wine_query = query.paginate(current_page, BaseConfig.PAGE_SIZE, False)

            wines = wine_query.items
            wines_json = [wine_jsonify(wine) for wine in wines]

            if current_page > wine_query.total or current_page < 1:
                return make_response({'msg': 'Page not found. It should be between 1 and the max number of pages'}, 404)

            url_next_page = ''
            if wine_query.has_next:
                base_url = request.url.split('page=')[0]
                suffix_url = request.url.split('page=')[1][1:]
                next_number_page = current_page+1
                url_next_page = base_url + f'page={next_number_page}' + suffix_url

            response = {
                'data': wines_json,
                'has_prev_page': wine_query.has_prev,
                'has_next_page': wine_query.has_next,
                'current_page': current_page,
                'num_pages': wine_query.total,
                'url_next_page': url_next_page
            }

            return make_response(
                jsonify(response), 200)
        except Exception as e:
            return make_response({'msg': 'bad request'}, 400)
