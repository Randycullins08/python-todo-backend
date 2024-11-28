from flask import request, jsonify

from models.todo import Todos, todo_schema, todos_schema
from util.helper_functions import dynamic_query
from util.reflection import populate_object
from db import db, query

def add_todo():
    post_data = request.get_json()

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
    
    return jsonify({"message" : "Todos found", "results" : todos_schema.dump(todo_data)}),201

def get_todo(todo_id):
    todo_data = dynamic_query(Todos, "todo_id", todo_id)

    if not todo_data:
        return jsonify({"message" : "No todos found"}), 404

    return jsonify({"message" : "Todo found", "results" : todo_schema.dump(todo_data)}),201

def update_todo(todo_id):
    todo_data = dynamic_query(Todos, 'todo_id', todo_id)
    post_data = request.form if request.form else request.get_json()

    populate_object(todo_data, post_data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message" : "Unable to update todo"}), 400

    return jsonify({"message" : "Todo updated", "result" : todo_schema.dump(todo_data)}),201

def delete_todo(todo_id):
    todo_data = dynamic_query(Todos, 'todo_id', todo_id)

    if not todo_data:
        return jsonify({"message" : "Todo not found"}),404

    try:
        db.session.delete(todo_data)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message" : "Unable to delete todo"}),400

    return jsonify({"message" : "Todo deleted"}),200

def update_todo_order():
    post_data = request.get_json()

    todo_data = db.session.query(Todos).all()

    new_order = post_data.get("newOrder", [])

    todo_data = new_order

    return jsonify({"message" : "Order Updated Successfully", "results" : todo_schema.dump(todo_data)}),201

