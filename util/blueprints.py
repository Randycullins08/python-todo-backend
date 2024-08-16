from routes.todo_routes import todos

def register_blueprint(app):
    app.register_blueprint(todos)