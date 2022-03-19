from tests.conftest import client


def test_status_code_request_200(client):
    response = client.get('/')
    assert response.status_code == 200


def test_request_display_example(client):
    response = client.get("/")
    data = response.data.decode()
    assert "Welcome to the GUDLFT Registration Portal!" in data


def test_login_with_email_valid(client):
    email = "john@simplylift.co"
    test_log = client.post('/showSummary', data={'email': email})
    assert test_log.status_code == 200


def test_user_email_unknown(client):
    email = "no_register_email@test.fr"
    test_log = client.post('/showSummary', data={'email': email}, follow_redirects=True)
    data = test_log.data.decode()
    assert "Welcome to the GUDLFT Registration Portal!" in data
    assert test_log.status_code == 200


