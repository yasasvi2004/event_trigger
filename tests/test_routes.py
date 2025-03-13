

import pytest
from app import create_app, db
from app.models import Trigger, EventLog
from datetime import datetime, timedelta

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://event_trigger_db_user:QZDwB0qVV33h0QPvHR11KbED7zIWfiBT@dpg-cv96ip52ng1s73d0mfcg-a.oregon-postgres.render.com/event_trigger_db'
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()
@pytest.fixture
def client(app):
    return app.test_client()

def test_create_scheduled_trigger(client):
    response = client.post('/triggers', json={
        'type': 'scheduled',
        'details': {'time': '2023-10-15T12:00:00Z'}
    })
    assert response.status_code == 201
    assert 'id' in response.json

def test_create_api_trigger(client):
    response = client.post('/triggers', json={
        'type': 'api',
        'details': {'endpoint': 'https://example.com/api', 'payload': {'key': 'value'}}
    })
    assert response.status_code == 201
    assert 'id' in response.json

def test_trigger_event(client):
    # Create a trigger
    client.post('/triggers', json={
        'type': 'api',
        'details': {'endpoint': 'https://example.com/api', 'payload': {'key': 'value'}}
    })
    # Trigger the event
    response = client.post('/triggers/1/trigger', json={'key': 'value'})
    assert response.status_code == 200
    assert response.json == {'message': 'Event triggered'}

def test_get_events(client):
    # Create and trigger an event
    client.post('/triggers', json={
        'type': 'api',
        'details': {'endpoint': 'https://example.com/api', 'payload': {'key': 'value'}}
    })
    client.post('/triggers/1/trigger', json={'key': 'value'})
    # Get events
    response = client.get('/events')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['trigger_id'] == 1