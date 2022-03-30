def test_not_allowed_booking_places_in_past_competition(client, captured_templates, mock_clubs,
                                                        mock_competitions):
    request = client.get('/book/Competition 1/Club 1')
    assert request.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert template.name == "welcome.html"
