from db import db

def dynamic_query(model, record_key, record_id):
    return db.session.query(model).filter(getattr(model, record_key) == record_id).first()