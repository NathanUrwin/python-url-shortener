import pytest

from src.app import app as flask_app


@pytest.fixture
def client():
    client = flask_app.test_client()
    yield client


def test_api(client):
    response = client.get('/')
    assert response._status_code == 200
