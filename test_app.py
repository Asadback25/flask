import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    # HTML faylda <title>Fibonacci Cal</title> mavjudligini tekshiramiz
    assert b"<title>Fibonacci Cal</title>" in response.data
