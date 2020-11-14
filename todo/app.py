from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
#from flask-RESTful import Resource, Api 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return "<h1> Hello World </h1>"


if __name__ == "__main__":
    app.run(debug=True)
