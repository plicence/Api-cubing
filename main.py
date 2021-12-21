from resource import Cube
from model.param import db, api, app


db.create_all()


api.add_resource(Cube, "/cubing/<int:cube_id>")
api.add_resource(Cube, "/cubing/<int:cuber_id>")
if __name__ == "__main__":
    app.run(debug=True)
