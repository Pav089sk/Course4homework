import json
from unittest.mock import mock_open, patch
from src.utils import read_json_data

@patch("json.load")
def test_transaction_data(mock_data):
    """Тест функция если в JSON файле корректный список"""
    mock_data.return_value = [{"id": 1, "amount": 100}]
    with patch("builtins.open"):
        result = read_json_data("test.json")
    assert result == [{"id": 1, "amount": 100}]
    mock_data.assert_called_once()