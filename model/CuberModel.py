from param import db


class CuberModel(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    cube_id = db.Column(db.Integer(), db.ForeignKey('cube.id'))
