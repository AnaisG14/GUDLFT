from flask import request, url_for


def test_display_index_for_request_index(client, captured_templates):
    """ Test url '/' and verify that the render template is 'index.html and
    the status of the request is 200.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert template.name == "index.html"


def test_login_with_email_valid(client, mock_clubs, captured_templates):
    """
    Test the login of a user is ok and redirect the user on the template
    'welcome.html'.
    """
    email = "club1@test.com"
    test_log = client.post('/showSummary', data={'email': email})
    data = test_log.data.decode()
    assert "Points available" in data
    assert test_log.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert context['club']['email'] == "club1@test.com"


def test_user_email_unknown(client, mock_clubs):
    """
    Test the redirection on template 'index.html' if the email user is
    not correct.
    """
    email = "no_register_email@test.fr"
    test_log = client.post('/showSummary', data={'email': email}, follow_redirects=True)
    data = test_log.data.decode()
    assert "Welcome to the GUDLFT Registration Portal!" in data
    assert test_log.status_code == 200


def test_user_logout(client, captured_templates):
    """
    Test if the user is redirect on 'index.html' if he logs out
    """
    response = client.get('/logout')
    assert response.status_code == 302
    client.get(url_for('index'))
    assert request.path == url_for('index')


