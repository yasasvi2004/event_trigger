from datetime import datetime, timedelta
from .extensions import db  # Import db from extensions.py
from .models import EventLog  # Import EventLog from models.py

def cleanup_old_events():
    old_events = EventLog.query.filter(EventLog.triggered_at < datetime.utcnow() - timedelta(hours=48)).all()
    for event in old_events:
        db.session.delete(event)
    db.session.commit()