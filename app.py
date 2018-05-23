from flask import Flask
from flask_restful import Resource, Api
from json import load, JSONEncoder
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import os

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Column
from sqlalchemy import DateTime, Integer, String, Text, Enum
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'questions.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Questions(db.Model,JSONEncoder): 
    def __init__(self,id,question):
        self.id = id
        self.question = question

    """An answer"""
    __tablename__          = "question"
    __table_args__         = {'sqlite_autoincrement': True}
    id                     = Column(Integer, primary_key=True, autoincrement=True)
    question               = Column(String(1024))


with open('questions.JSON') as f:
    data = load(f)

class Root(Resource):
    def get(self):
        return { "version": 1, "description": "blah blah blah" } # Change me! description

class Questions(Resource):
    def get(self):
        return list(map(lambda x:x['id'], data['questions']))

class Question_id(Resource):
    def get(self, question_id):
        return data['questions'][0] # Change me! question id not array index needed

api.add_resource(Root, '/')
api.add_resource(Questions, '/questions')
api.add_resource(Question_id, '/questions/<string:question_id>')

if __name__ == '__main__':
    app.run(debug=True)
