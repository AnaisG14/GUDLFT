from tests.conftest import client, mock_clubs, mock_competitions
from server import purchase_places


def test_updating_points_after_purchase_places(client, mock_clubs, mock_competitions):
    request = client.post('/purchasePlaces', data={'places': '4', 'competition': 'Competition 1', 'club': 'Club 1'})
    data = request.data.decode()
    # mocks_club1 has 10 points, it must have 6 after the purchase
    assert 'Points available: 6' in data


