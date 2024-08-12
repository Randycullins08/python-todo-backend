import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Todos(db.Model):
    __tablename__ = "Todos"

    todo_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    task = db.Column(db.String(), nullable=False, unique=True)
    completed = db.Column(db.Boolean(), nullable=False, default=False)

    def __init__(self, task):
        self.task = task