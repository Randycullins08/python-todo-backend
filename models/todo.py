import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db

class Todos(db.Model):
    __tablename__ = "Todos"

    todo_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    task = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean(), nullable=False, default=False)

    def __init__(self, task):
        self.task = task

    def new_todo_obj():
        return Todos("")

class TodosSchema(ma.Schema):
    class Meta:
        fields = ['todo_id', 'task', 'completed']

todo_schema = TodosSchema()
todos_schema = TodosSchema(many=True)