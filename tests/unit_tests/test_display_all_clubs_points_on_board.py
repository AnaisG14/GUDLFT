class TestDisplayAllClubsPointsOnBoard:
    """
    Test url '/board' render on template 'board.html and display all clubs and
    their available points.
    """

    def test_request_render_board(self, client, captured_templates, mock_clubs):
        """ Test request '/board' render the template 'board.html'"""
        request = client.get('/board')
        assert request.status_code == 200
        template, context = captured_templates[0]
        assert template.name == 'board.html'
        data = request.data.decode()
        assert "Summary of points' clubs" in data
        assert "Club 1 : points available = 10" in data
