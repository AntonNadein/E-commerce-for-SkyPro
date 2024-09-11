import unittest
from unittest.mock import patch

import pytest

from src.product import Product


def test_product(test_product_data):
    assert test_product_data.name == "test"
    assert test_product_data.description == "test_description"
    assert test_product_data.price == 50.50
    assert test_product_data.quantity == 5


def test_price_setter(capsys, test_product_data):
    test_product_data.price = 60
    assert test_product_data.price == 60
    test_product_data.price = 0
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"
    test_product_data.price = -50
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_new_product():
    test_dict = {"name": "test1", "description": "test2", "price": 500, "quantity": 5}
    new_product = Product.new_product(test_dict)
    assert new_product.name == "test1"
    assert new_product.description == "test2"
    assert new_product.price == 500
    assert new_product.quantity == 5


class TestTripleQuestion(unittest.TestCase):

    @patch("builtins.input", side_effect=["yes"])
    def test_price_setter_input_yes(self, mock_input):
        test_products = Product("test", "test_description", 50.50, 5)
        test_products.price = 50
        assert test_products.price == 50

    @patch("builtins.input", side_effect=["no"])
    def test_price_setter_input_no(self, mock_input):
        test_products = Product("test", "test_description", 50.50, 5)
        test_products.price = 50
        assert test_products.price == 50.50


def test_str_product(test_product_data):
    assert str(test_product_data) == "test, 50.5руб. Остаток: 5шт."


def test_add_product(test_product_1_add, test_product_2_add):
    assert test_product_1_add + test_product_2_add == 2137000.0


def test_product_quantity_0():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Redmi", "Смартфон Redmi", 250, 0)
