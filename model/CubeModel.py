from param import db


class CubeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    magnetic = db.Column(db.Boolean, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    cuber = db.relationship('CuberModel', lazy="dynamic")

    def __repr__(self):
        return f"Video(name =" + self.name + ", " + self.magnetic + " " + self.brand

