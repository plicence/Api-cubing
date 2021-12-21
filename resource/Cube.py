from flask_restful import Resource, reqparse, fields, marshal_with, abort
from model import CubeModel
from model.param import db

cubing_put_args = reqparse.RequestParser()
cubing_put_args.add_argument("Name", type=str, help="Cube name required", required="True")
cubing_put_args.add_argument("Magnetic", type=bool, help="Magnetic required")
cubing_put_args.add_argument("Size", type=int, help="Size required")
cubing_put_args.add_argument("Brand", type=str, help="Cube brand required")
cubing_put_args.add_argument("Cuber", type="id")

cubing_update_args = reqparse.RequestParser()
cubing_put_args.add_argument("Name", type=str, help="Cube name required")
cubing_put_args.add_argument("Magnetic", type=bool, help="Magnetic required")
cubing_put_args.add_argument("Size", type=int, help="Size required")
cubing_put_args.add_argument("Brand", type=str, help="Cube brand required")

resource_fields = {
    'id:': fields.Integer,
    'name': fields.String,
    'magnetic': fields.Boolean,
    'size': fields.Integer,
    'brand': fields.String,
    'cuber': fields.Integer
}


class Cube(Resource):
    @marshal_with(resource_fields)
    def get(self, cube_id):
        result = CubeModel.query.filter_by(id=cube_id).first()
        return result

    @marshal_with(resource_fields)
    def put(self, cube_id):
        args = cubing_put_args.parse_args()
        print("args", args)
        result = CubeModel.query.filter_by(id=cube_id).first()
        if result:
            abort(409, message="Video id taken")
        cube = CubeModel(id=cube_id, name=args["Name"], magnetic=args["Magnetic"], size=args["Size"],
                         brand=args["Brand"], cuber=args["Cuber"])
        print("args:", args["Name"])
        # print("After model : ", cube.id, cube.name, cube.magnetic, cube.size, cube.brand)
        print("why dont i go there ???")
        db.session.add(cube)
        db.session.commit()
        return cube, 201