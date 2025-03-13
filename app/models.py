from .extensions import db  # Import db from extensions.py

class Trigger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    details = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class EventLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trigger_id = db.Column(db.Integer, db.ForeignKey('trigger.id'), nullable=False)
    triggered_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    payload = db.Column(db.JSON)
    is_test = db.Column(db.Boolean, default=False)