from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

global app
app = Flask(__name__)
global api
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/database.db'
global db
db = SQLAlchemy(app)