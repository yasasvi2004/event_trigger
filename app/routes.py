from flask import request, jsonify, current_app
from .extensions import db  # Import db from extensions.py
from .models import Trigger, EventLog  # Import Trigger from models.py
from .scheduler import add_scheduled_trigger  # Import add_scheduled_trigger from scheduler.py
from datetime import datetime, timedelta
from flask import Blueprint
import logging

main = Blueprint('main', __name__)
@main.route('/triggers', methods=['POST'])
def create_trigger():
    data = request.json
    trigger_type = data.get('type')
    details = data.get('details')

    if trigger_type not in ['scheduled', 'api']:
        return jsonify({'error': 'Invalid trigger type'}), 400

    # Create the trigger in the database
    trigger = Trigger(type=trigger_type, details=details)
    db.session.add(trigger)
    db.session.commit()

    # Schedule the trigger if it's a scheduled trigger
    if trigger_type == 'scheduled':
        add_scheduled_trigger(current_app._get_current_object(), trigger.id, details)

    return jsonify({'id': trigger.id}), 201

@main.route('/triggers/<int:trigger_id>/trigger', methods=['POST'])
def trigger_event(trigger_id):
    trigger = db.session.get(Trigger, trigger_id)
    payload = request.json if trigger.type == 'api' else None

    event = EventLog(trigger_id=trigger.id, payload=payload, is_test=False)
    db.session.add(event)
    db.session.commit()

    return jsonify({'message': 'Event triggered'}), 200

@main.route('/events', methods=['GET'])
def get_events():
    aggregate = request.args.get('aggregate', default=None)
    logging.info(f"Aggregate parameter: {aggregate}")  # Debugging

    if aggregate is not None:
        # Convert the `aggregate` parameter to a boolean
        aggregate = aggregate.lower() == 'true'

    if aggregate:
        # Aggregate event logs by trigger_id
        events = db.session.query(
            EventLog.trigger_id,
            db.func.count(EventLog.id).label('count')
        ).filter(
            EventLog.triggered_at >= datetime.utcnow() - timedelta(hours=48)
        ).group_by(
            EventLog.trigger_id
        ).all()

        logging.info(f"Aggregated events: {events}")  # Debugging
        return jsonify([{
            'trigger_id': event.trigger_id,
            'count': event.count
        } for event in events]), 200
    else:
        # Return individual event logs
        events = EventLog.query.filter(EventLog.triggered_at >= datetime.utcnow() - timedelta(hours=48)).all()
        logging.info(f"Individual events: {events}")  # Debugging
        return jsonify([{
            'id': event.id,
            'trigger_id': event.trigger_id,
            'triggered_at': event.triggered_at.isoformat(),
            'payload': event.payload,
            'is_test': event.is_test
        } for event in events]), 200