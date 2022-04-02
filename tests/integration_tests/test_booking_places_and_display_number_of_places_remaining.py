def test_booking_places_and_display_number_of_places_remaining(client, captured_templates, mock_competitions, mock_clubs):
    """
    Book places in competition and
    verify that welcome page display the right competition places.
    """
    first_booking_places = {'places': '5', 'competition': 'Competition 2', 'club': 'Club 1'}
    request_book = client.post('/purchasePlaces', data = first_booking_places)
    assert request_book.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert int(context['competitions'][1]['numberOfPlaces']) == 8