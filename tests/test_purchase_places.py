from server import transform_string_in_datetime
import pytest


class TestPurchasePlaces:
    booking_places = {'places': '4', 'competition': 'Competition 2', 'club': 'Club 1'}
    booking_places_over_12 = {'places': '14', 'competition': 'Competition 2', 'club': 'Club 1'}
    booking_more_places_than_points = {'places': '11', 'competition': 'Competition 2', 'club': 'Club 1'}

    @staticmethod
    def _test_request(request, captured_templates):
        request = request
        assert request.status_code == 200
        assert len(captured_templates) == 1
        template, context = captured_templates[0]
        return template, context

    def test_updating_points_after_purchase_places(self, client, captured_templates, mock_clubs, mock_competitions):
        request = client.post('/purchasePlaces', data=self.booking_places)
        # mocks_club1 has 10 points, it must have 6 after the purchase
        template, context = self._test_request(request, captured_templates)
        assert template.name == "welcome.html"
        assert context["club"]['points'] == 6

    def test_booking_places_in_a_competition(self, client, captured_templates, mock_clubs, mock_competitions):
        request = client.get('/book/Competition 2/Club 2')
        template, context = self._test_request(request, captured_templates)
        assert template.name == "booking.html"

    def test_not_allowed_booking_places_in_past_competition(self, client, captured_templates, mock_clubs, mock_competitions):
        request = client.get('/book/Competition 1/Club 1')
        template, context = self._test_request(request, captured_templates)
        assert template.name == "welcome.html"

    def test_booking_places(self, client, captured_templates, mock_clubs, mock_competitions):
        request = client.post('/purchasePlaces', data=self.booking_places)
        template, context = self._test_request(request, captured_templates)
        assert template.name == "welcome.html"
        data = request.data.decode()
        assert 'Great-booking complete' in data

    def test_booking_no_more_than_12_places_per_competition(self, client, captured_templates, mock_clubs, mock_competitions):
        request = client.post('/purchasePlaces', data=self.booking_places_over_12)
        template, context = self._test_request(request, captured_templates)
        assert template.name == "welcome.html"
        data = request.data.decode()
        assert "You cannot book more than 12 places for one competition. The transaction is aborted." in data
        assert int(context["competitions"][1]['numberOfPlaces']) == 13

    def test_impossible_booking_more_than_club_points(self, client, captured_templates, mock_clubs, mock_competitions):
        request = client.post('/purchasePlaces', data=self.booking_more_places_than_points)
        template, context = self._test_request(request, captured_templates)
        assert template.name == "welcome.html"
        data = request.data.decode()
        assert "You do not have enough points. The transaction is aborted." in data
        assert int(context['competitions'][1]['numberOfPlaces']) == 13
        assert int(context['club']['points']) == 10

    def test_transform_string_datetime_in_datetime(self):
        string_datetime = "2022-03-20 10:00:00"
        new_datetime, today_datetime = transform_string_in_datetime(string_datetime)
        assert str(new_datetime) == string_datetime

    @pytest.mark.parametrize("url_link", ['/book/Competition 3/Club 1', '/book/Competition 2/Club 3'])
    def test_book_with_wrong_club_or_wrong_competition(self, url_link, client, captured_templates, mock_clubs, mock_competitions):
        request = client.get(url_link)
        template, context = self._test_request(request, captured_templates)
        assert template.name == "welcome.html"
        data = request.data.decode()
        assert "Something went wrong-please try again" in data
