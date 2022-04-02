def test_booking_places_in_two_competition(client, captured_templates, mock_competitions, mock_clubs):
    first_booking_places = {'places': '4', 'competition': 'Competition 2', 'club': 'Club 1'}
    second_booking_places = {'places': '5', 'competition': 'Competition 20', 'club': 'Club 1'}

    request1 = client.post('/purchasePlaces', data=first_booking_places)
    assert request1.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert int(context['club']['points']) == 6
    assert int(context['competitions'][1]['numberOfPlaces']) == 9

    request_book = client.get('/book/Competition 20/Club 1')
    assert request_book == 200
    assert len(captured_templates) == 2

    request2 = client.post('/purchasePlaces', data=second_booking_places)
    assert request2.status_code == 200
    assert len(captured_templates) == 3
    template, context = captured_templates[2]
    assert int(context['club']['points']) == 1
    assert int(context['competitions'][2]['numberOfPlaces']) == 12



# book places in competition 2
# logout
# login
# verify that places already booked in competition are deducted
