from flask import Blueprint

from controllers import todo_controller

todos = Blueprint('todos', __name__)

@todos.route('/todos', methods=['POST'])
def add_todo():
    return todo_controller.add_todo()