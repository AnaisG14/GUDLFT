from tests.conftest import client, data_club_json, data_competition_json
import server


def test_status_code_request_200(client):
    response = client.get('/')
    assert response.status_code == 200


def test_request_display_example(client):
    response = client.get("/")
    data = response.data.decode()
    assert "Welcome to the GUDLFT Registration Portal!" in data


def test_login_with_email_valid(client, mocker, data_club_json):
    email = "club1@test.com"
    mocker.patch.object(server, 'clubs', data_club_json)
    test_log = client.post('/showSummary', data={'email': email})
    data = test_log.data.decode()
    assert "Points available" in data
    assert test_log.status_code == 200


def test_user_email_unknown(client, mocker, data_club_json):
    email = "no_register_email@test.fr"
    mocker.patch.object(server, 'clubs', data_club_json)
    test_log = client.post('/showSummary', data={'email': email}, follow_redirects=True)
    data = test_log.data.decode()
    assert "Welcome to the GUDLFT Registration Portal!" in data
    assert test_log.status_code == 200


