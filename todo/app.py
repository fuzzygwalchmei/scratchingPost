from flask import Flask, request, abort, render_template
from flask_sqlalchemy import SQLAlchemy
#from flask-RESTful import Resource, Api 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.sqlite3'
db = SQLAlchemy(app)

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

@app.route('/')
def home():
    return "<h1> Hello World </h1>"

@app.route('/all')
def all():
    todos = ToDo.query.all()
    return render_template('show_stuff.html', todos = todos)

@app.route('/<id>')
def single(id):
    todo = ToDo.query.filter(ToDo.id == id)
    return render_template('show_stuff.html', todos = todo)


if __name__ == "__main__":
    app.run(debug=True)
