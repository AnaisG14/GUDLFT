from unittest.mock import mock_open, patch
import pytest


@pytest.mark.parametrize('file', ['clubs.json', 'competitions.json'])
def test_loading_clubs_and_competitions(file):
    with patch('builtins.open', mock_open(read_data='data')) as mock_file:
        assert open(file).read() == 'data'
    mock_file.assert_called_with(file)


