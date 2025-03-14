from apscheduler.schedulers.background import BackgroundScheduler
from .extensions import db  # Import db from extensions.py
from .models import EventLog  # Import EventLog from models.py
import logging
from datetime import datetime, timedelta

# Initialize the scheduler
scheduler = BackgroundScheduler()

from apscheduler.triggers.interval import IntervalTrigger

def add_scheduled_trigger(app, trigger_id, details):
    logging.info(f"Scheduling trigger for {trigger_id} with details: {details}")
    try:
        if 'time' in details:
            logging.info(f"Adding one-time trigger for {trigger_id} at {details['time']}")
            scheduler.add_job(
                trigger_scheduled_event,
                'date',
                run_date=details['time'],
                args=[app, trigger_id]
            )
        elif 'interval' in details:
            recurring = details.get('recurring', False)
            if recurring:
                logging.info(f"Adding recurring trigger for {trigger_id} with interval {details['interval']} minutes")
                scheduler.add_job(
                    trigger_scheduled_event,
                    IntervalTrigger(minutes=details['interval']),
                    args=[app, trigger_id]
                )
            else:
                logging.info(f"Adding one-time trigger for {trigger_id} with delay of {details['interval']} minutes")
                scheduler.add_job(
                    trigger_scheduled_event,
                    'date',
                    run_date=datetime.utcnow() + timedelta(minutes=details['interval']),
                    args=[app, trigger_id]
                )
    except Exception as e:
        logging.error(f"Error scheduling job: {e}")

def trigger_scheduled_event(app, trigger_id):
    logging.info(f"trigger_scheduled_event called with trigger_id: {trigger_id}")
    try:
        with app.app_context():
            logging.info(f"Executing scheduled event for trigger ID: {trigger_id}")
            event = EventLog(trigger_id=trigger_id, is_test=False)
            db.session.add(event)
            db.session.commit()
            logging.info("Event logged successfully.")
    except Exception as e:
        logging.error(f"Error executing scheduled event for trigger_id {trigger_id}: {e}")