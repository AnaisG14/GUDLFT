from tests.conftest import client, mock_clubs, mock_competitions
from server import purchase_places
import server


class TestPurchasePlaces:
    booking_places = {'places': '4', 'competition': 'Competition 1', 'club': 'Club 1'}

    def test_updating_points_after_purchase_places(self, client, captured_templates, mock_clubs, mock_competitions):
        request = client.post('/purchasePlaces', data=self.booking_places)
        # mocks_club1 has 10 points, it must have 6 after the purchase
        assert request.status_code == 200
        assert len(captured_templates) == 1
        template, context = captured_templates[0]
        assert template.name == "welcome.html"
        assert context["club"]['points'] == 6

    def test_booking_places_in_a_competition(self, client, captured_templates, mock_clubs, mock_competitions):
        request = client.get('/book/Competition 2/Club 2')
        assert request.status_code == 200
        assert len(captured_templates) == 1
        template, context = captured_templates[0]
        assert template.name == "booking.html"

    def test_not_allowed_booking_places_in_past_competition(self, client, captured_templates, mock_clubs, mock_competitions):
        request = client.get('/book/Competition 1/Club 1')
        assert request.status_code == 200
        assert len(captured_templates) == 1
        template, context = captured_templates[0]
        assert template.name == "welcome.html"



