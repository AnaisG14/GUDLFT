class TestDisplayAllClubsPointsOnBoard:
    """
    Test url '/board' render on template 'board.html and display all clubs and
    their available points.
    """

    def test_request_render_board(self, client, captured_templates):
        """ Test request '/board' render on template 'board.html'"""
        request = client.get('/board')
        assert request.status_code == 200
        template, context = captured_templates[0]
        assert template.name == 'board.html'


    # test that all clubs are display


    # test display name and points for each club
