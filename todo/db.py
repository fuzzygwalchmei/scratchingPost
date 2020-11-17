import sqlalchemy
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_marshmallow import Marshmallow


app=Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.sqlite3'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class ToDo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String)
    note = db.Column(db.String)

    def __init__(self, subject, note):
        self.subject = subject
        self.note = note

    def __repr__(self):
        return f'<ToDo(id: {self.id} - note: {self.note}'
db.create_all()

class TodoSchema(ma.Schema):
    class Meta:
        fields = ("id", "subject", "note")
        model = ToDo
    
todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)




def get_connection():
    pass


class TodoAPI(Resource):
    def get(self):
        todos = ToDo.query.all()
        return todos_schema.dump(todos)

    def get(self, id):
        todo = ToDo.query.get_or_404(id)
        return todo_schema.dump(todo)

    def post(self):
        new_todo = ToDo(
            subject = request.json['subject'],
            note = request.json['note']
        )
        db.session.add(new_todo)
        db.session.commit()
        return todo_schema.dump(new_todo)

    def update_item(self, id):
        pass

    def delete_item(self, id):
        pass

api.add_resource(TodoAPI, '/todo/api/v1.0/todos', endpoint = 'todos')
api.add_resource(TodoAPI, '/todo/api/v1.0/todos/<int:id>', endpoint = 'todo')

if __name__ == "__main__":
    app.run(debug=True)