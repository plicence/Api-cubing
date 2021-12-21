from model.CuberModel import CuberModel
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from main.param import db

cuber_put_args = reqparse.RequestParser()
cuber_put_args.add_argument("name", type=str, help="Cube name required", required="True")
cuber_put_args.add_argument("age", type=int, help="Magnetic required")
cuber_put_args.add_argument("cube_id", type=int, help="Size required")

resource_fields = {
    'id:': fields.Integer,
    'name': fields.String,
    'magnetic': fields.Boolean,
    'size': fields.Integer,
    'brand': fields.String,
    'cuber': fields.Integer
}


class Cuber(Resource):
    @marshal_with(resource_fields)
    def get(self, cuber_id):
        result = CuberModel.query.filter_by(id=cuber_id).first()
        return result

    @marshal_with(resource_fields)
    def put(self, cuber_id):
        print("I got herre")

        args = cuber_put_args.parse_args()
        print("args", args)
        result = CuberModel.query.filter_by(id=cuber_id).first()
        if result:
            abort(409, message="Video id taken")
        cuber = CuberModel(id=cuber_id, name=args["name"], age=args["age"], cube_id=args["cube_id"])
        print("args:", args["Name"])
        # print("After model : ", cube.id, cube.name, cube.magnetic, cube.size, cube.brand)
        print("why dont i go there ???")
        db.session.add(cuber)
        db.session.commit()
        return cuber, 201