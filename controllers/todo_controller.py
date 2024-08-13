from flask import jsonify
from models.todo import Todos, todo_schema, todos_schema
from db import *
from util import populate_object

def create_todo():
    post_data = request.form if request.form else request.get_json()

    new_todo = Todos.new_todo_obj()
    populate_object(new_todo, post_data)

    try:
        db.session.add(new_todo)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message" : "unable to create record"}), 400

    return jsonify({"message" : "Todo Created", "results" : todo_schema.dump(new_todo)}), 201