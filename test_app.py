import pytest
from app_wrapper.app import app



@pytest.fixture
def client():
    print(app)
    """Create a test client for the Flask app."""
    return app.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello World!"