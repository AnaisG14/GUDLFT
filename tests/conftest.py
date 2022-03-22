import pytest
import server


@pytest.fixture
def client():
    server.app.config.update({"TESTING": True})
    with server.app.test_client() as client:
        yield client


@pytest.fixture
def data_club_json():
    data = [
        {
            "name": "Club 1",
            "email": "club1@test.com",
            "points": "1"
        },
        {
            "name": "Club 2",
            "email": "club2@test.com",
            "points": "2"
        }
    ]
    return data


@pytest.fixture
def data_competition_json():
    data = [
        {
            "name": "Competition 1",
            "date": "2022-03-20 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Competition 2",
            "date": "2022-05-22 10:00:00",
            "numberOfPlaces": "13"
        }
    ]
    return data
