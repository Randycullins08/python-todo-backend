from flask import Blueprint

from controllers import todo_controller

todos = Blueprint('todos', __name__)

@todos.route('/todos', methods=['POST'])
def add_todo():
    return todo_controller.add_todo()

@todos.route('/todos', methods=['GET'])
def get_todos():
    return todo_controller.get_todos()

@todos.route('/todo/<todo_id>', methods=['GET'])
def get_one_todo(todo_id):
    return todo_controller.get_todo(todo_id)

@todos.route('/todo/<todo_id>', methods=['PUT'])
def update_todo(todo_id):
    return todo_controller.update_todo(todo_id)

@todos.route('/todo/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    return todo_controller.delete_todo(todo_id)

@todos.route('/todos/order', methods=['POST'])
def update_todo_order():
    return todo_controller.update_todo_order()