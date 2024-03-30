import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_predict_popularity(client):
    # Example test for the predict endpoint
    response = client.post('/predict', json={'budget': 100000000, 'runtime': 120})
    assert response.status_code == 200
    assert 'popularity' in response.json
