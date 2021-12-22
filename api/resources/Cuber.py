from flask_restful import Resource, marshal_with, fields, reqparse

from api.models.CuberModel import CuberModel
from param import db

cuber_put_args = reqparse.RequestParser()
cuber_put_args.add_argument("name", type=str, required=True)
cuber_put_args.add_argument("age", type=int)



resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'age': fields.Integer


}

class Cuber(Resource):

    @marshal_with(resource_fields)
    def get(self, cuber_id):
        result = CuberModel.query.filter_by(id=cuber_id).first()
        return result

    @marshal_with(resource_fields)
    def put(self, cuber_id):
        args = cuber_put_args.parse_args()
        cuber = CuberModel(id=cuber_id, name=args["name"], age=args["age"])
        db.session.add(cuber)
        db.session.commit()
        return cuber, 201