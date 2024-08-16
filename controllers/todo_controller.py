from flask import request, jsonify

from models.todo import Todos, todo_schema, todos_schema
from util.reflection import populate_object
from db import db, query

def add_todo():
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

def get_todos():
    todo_data = db.session.query(Todos).all()

    if not todo_data:
        return jsonify({"message" : "No todos found"}), 404
    
    return jsonify({"message" : "Todos found", "results" : todos_schema.dump(todo_data)}),201

def get_todo(todo_id):
    todo_data = db.session.query(Todos).filter(Todos.todo_id == todo_id).first()
    print(todo_id)

    if not todo_data:
        return jsonify({"message" : "No todos found"}), 404

    return jsonify({"message" : "Todo found", "results" : todo_schema.dump(todo_data)}),201