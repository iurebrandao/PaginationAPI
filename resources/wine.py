from flask_restful import Resource


class Wine(Resource):

    def get(self):
        return {'hello': 'world'}