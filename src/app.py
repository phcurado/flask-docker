from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

db = SQLAlchemy(app)


@app.route('/')
def homepage():
    return jsonify(hello='world!')

@app.route("/user/<name>")
def get_user_name(name):
    return "Hello {}".format(name)

if __name__ == '__main__':
    app.run()