from unittest.mock import patch

from src.utils import category_to_list, open_json


def test_category_to_list(test_category_to_list_data):
    result = category_to_list(test_category_to_list_data)
    assert result[0].name == "Смартфоны"
    assert (len(result[0].products)) == 2


@patch("json.load")
def test_simple_search(mock_file):
    mock_file.return_value = {"user_simple_search": "test_1"}
    result = open_json("data/products.json")
    assert result == {"user_simple_search": "test_1"}
