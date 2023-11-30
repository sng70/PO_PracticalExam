import json
import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_read_users_status_code(client):
    response = client.get('/users')
    assert response.status_code == 200

def test_read_users_data_type(client):
    response = client.get('/users')
    data = json.loads(response.get_data(as_text=True))
    assert isinstance(data, list)

def test_read_user_status_code(client):
    response = client.get('/users/1')
    assert response.status_code == 200

def test_read_user_data_type(client):
    response = client.get('/users/1')
    data = json.loads(response.get_data(as_text=True))
    assert isinstance(data, dict)

def test_read_user_not_found_status_code(client):
    response = client.get('/users/999')
    assert response.status_code == 404

def test_read_user_not_found_data(client):
    response = client.get('/users/999')
    data = json.loads(response.get_data(as_text=True))
    assert 'error' in data

def test_create_user_status_code(client):
    user_data = {"name": "John", "lastname": "Doe"}
    response = client.post('/')