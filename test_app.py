import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

    data = response.get_json()
    assert data["service"] == "Waste Management Service"
    assert data["status"] == "running"


def test_get_waste(client):
    response = client.get("/waste")
    assert response.status_code == 200

    data = response.get_json()
    assert "waste" in data
    assert len(data["waste"]) > 0


def test_schedule(client):
    response = client.get("/schedule")
    assert response.status_code == 200

    data = response.get_json()
    assert "schedule" in data
    assert len(data["schedule"]) > 0