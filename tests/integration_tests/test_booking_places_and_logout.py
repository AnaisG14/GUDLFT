from flask import url_for


def test_booking_places_and_logout(client, captured_templates, mock_clubs, mock_competitions):
    """Test after booking places, you can log out and return to the login page"""

    booking_places = {'places': '7', 'competition': 'Competition 2', 'club': 'Club 1'}
    client.post('/purchasePlaces', data=booking_places)
    client.get('/logout')
    request_logout = client.get(url_for("index"))
    assert request_logout.status_code == 200
    template, context = captured_templates[1]
    print('template', template)
    assert template.name == 'index.html'
