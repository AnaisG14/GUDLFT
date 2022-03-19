from server import load_clubs, load_competitions


def test_clubs_loaded_in_list():
    list_of_clubs = load_clubs()
    assert type(list_of_clubs) == list
    assert type(list_of_clubs[0]) == dict
    assert list_of_clubs[0]['name']
    assert list_of_clubs[0]['email']
    assert list_of_clubs[0]['points']


def test_competition_loaded_in_list():
    list_of_competitions = load_competitions()
    assert type(list_of_competitions) == list
    assert type(list_of_competitions[0]) == dict
    assert list_of_competitions[0]['name']
    assert list_of_competitions[0]['date']
    assert list_of_competitions[0]['numberOfPlaces']

