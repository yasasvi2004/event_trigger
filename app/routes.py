from flask import request, jsonify, current_app
from .extensions import db  # Import db from extensions.py
from .models import Trigger, EventLog  # Import Trigger from models.py
from .scheduler import add_scheduled_trigger  # Import add_scheduled_trigger from scheduler.py
from datetime import datetime, timedelta
from flask import Blueprint

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
    trigger = Trigger.query.get_or_404(trigger_id)
    payload = request.json if trigger.type == 'api' else None

    event = EventLog(trigger_id=trigger.id, payload=payload, is_test=False)
    db.session.add(event)
    db.session.commit()

    return jsonify({'message': 'Event triggered'}), 200

@main.route('/events', methods=['GET'])
def get_events():
    events = EventLog.query.filter(EventLog.triggered_at >= datetime.utcnow() - timedelta(hours=2)).all()
    return jsonify([{
        'id': event.id,
        'trigger_id': event.trigger_id,
        'triggered_at': event.triggered_at,
        'payload': event.payload,
        'is_test': event.is_test
    } for event in events]), 200

