import pytest
import logging
from app import create_app
from app.extensions import db
from app.models import Trigger, EventLog
import os

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_trigger(client):
    logging.info("Running test_create_trigger")
    response = client.post('/triggers', json={
        'type': 'scheduled',
        'details': {'time': '2025-03-14T08:27:10Z'}
    })
    assert response.status_code == 201
    assert 'id' in response.json

def test_trigger_event(client):
    logging.info("Running test_trigger_event")
    # First, create a trigger
    response = client.post('/triggers', json={
        'type': 'api',
        'details': {}
    })
    assert response.status_code == 201
    trigger_id = response.json['id']

    # Trigger the event
    response = client.post(f'/triggers/{trigger_id}/trigger', json={'key': 'value'})
    assert response.status_code == 200
    assert response.json == {'message': 'Event triggered'}

def test_get_events(client):
    logging.info("Running test_get_events")
    # First, create a trigger and trigger an event
    response = client.post('/triggers', json={
        'type': 'api',
        'details': {}
    })
    assert response.status_code == 201
    trigger_id = response.json['id']

    response = client.post(f'/triggers/{trigger_id}/trigger', json={'key': 'value'})
    assert response.status_code == 200

    # Get events
    response = client.get('/events')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['trigger_id'] == trigger_id