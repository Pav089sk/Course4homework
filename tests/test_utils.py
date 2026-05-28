from unittest.mock import patch

from src.utils import creator_from_json, read_json_data


@patch("json.load")
def test_transaction_data(mock_data):
    """Тест функция если в JSON файле корректный список"""
    mock_data.return_value = [{"id": 1, "amount": 100}]
    with patch("builtins.open"):
        result = read_json_data("test.json")
    assert result == [{"id": 1, "amount": 100}]
    mock_data.assert_called_once()


def test_creator(data_for_test):
    assert creator_from_json(data_for_test)[0].name == "Телевизоры"
    assert creator_from_json(data_for_test)[0].products == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'
