from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import psycopg2

from db import *
import os

from models.todo import Todos, todo_schema, todos_schema
from util.blueprints import register_blueprint
import routes

flask_host = os.environ.get("FLASK_HOST")
flask_port = os.environ.get("FLASK_POST")

database_scheme = os.environ.get("DATABASE_SCHEME")
database_user = os.environ.get("DATABASE_USER")
database_address = os.environ.get("DATABASE_ADDRESS")
database_port = os.environ.get("DATABASE_PORT")
database_name = os.environ.get("DATABASE_NAME")

app = Flask(__name__)
register_blueprint(app)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = f"{database_scheme}{database_user}@{database_address}:{database_port}/{database_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app, db)
ma = Marshmallow(app)

def create_tables():
    with app.app_context():
        print("Creating tables...")
        db.create_all()
        print("Tables created successfully")

create_tables()

if __name__ == '__main__':
    app.run(host=flask_host, port=flask_port)