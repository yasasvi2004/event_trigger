import time
import logging
from app import create_app
from .extensions import db
from .models import EventLog
from datetime import datetime, timedelta

app = create_app()

def process_scheduled_events():
    with app.app_context():
        while True:
            # Check for scheduled events and process them
            events = EventLog.query.filter(EventLog.triggered_at <= datetime.utcnow()).all()
            for event in events:
                logging.info(f"Processing event: {event.id}")
                # Perform the task (e.g., send an email, call an API, etc.)
                # Mark the event as processed
                db.session.delete(event)
                db.session.commit()
            time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    process_scheduled_events()