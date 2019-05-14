from flask import Blueprint
from flask_restful import Resource, Api, reqparse
from generator.iching import PyChing

bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(bp)

parser = reqparse.RequestParser()


class ApiRoot(Resource):
    def get(self, iterations, sets):
        experiment = PyChing(iterations=iterations, sets=sets)
        results = experiment.run()
        return results


api.add_resource(ApiRoot, '/<int:iterations>/<int:sets>')


