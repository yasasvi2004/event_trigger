from apscheduler.schedulers.background import BackgroundScheduler
from .extensions import db  # Import db from extensions.py
from .models import EventLog  # Import EventLog from models.py
import logging

# Initialize the scheduler
scheduler = BackgroundScheduler()

def add_scheduled_trigger(app, trigger_id, details):
    logging.info(f"Scheduling trigger for {trigger_id} with details: {details}")
    try:
        if 'time' in details:
            scheduler.add_job(trigger_scheduled_event, 'date', run_date=details['time'], args=[app, trigger_id])
        elif 'interval' in details:
            scheduler.add_job(trigger_scheduled_event, 'interval', minutes=details['interval'], args=[app, trigger_id])
    except Exception as e:
        logging.error(f"Error scheduling job: {e}")

def trigger_scheduled_event(app, trigger_id):
    try:
        # Use the passed Flask app to create an application context
        with app.app_context():
            logging.info(f"Executing scheduled event for trigger ID: {trigger_id}")
            event = EventLog(trigger_id=trigger_id, is_test=False)
            db.session.add(event)
            db.session.commit()
    except Exception as e:
        logging.error(f"Error executing scheduled event for trigger_id {trigger_id}: {e}")
scheduler.start()