from flask_restful import reqparse, fields
from api.resources.Cuber import Cuber
from param import db, api, app



db.create_all()

cuber_put_args = reqparse.RequestParser()
cuber_put_args.add_argument("name", type=str, help="Cube name required", required="True")
cuber_put_args.add_argument("age", type=int, help="Magnetic required")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'age': fields.Integer
}

api.add_resource(Cuber, "/cuber/<int:cuber_id>")

if __name__ == "__main__":
    app.run(debug=True)
print("test")
