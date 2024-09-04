import pytest

from src.category import Category
from src.product import Product


def test_str_category(test_category_data):
    assert str(test_category_data) == "test_category, количество продуктов: 59 шт."


def test_category(test_category_data, test_second_category_data):
    assert test_category_data.name == "test_category"
    assert test_category_data.description == "test_description"
    assert Category.product_count == 4
    assert Category.category_count == 3


def test_products_property(test_category_data):
    assert test_category_data.products == (
        "Xiaomi Redmi Note 11, 31000.0руб. Остаток: 15шт.\n" "Xiaomi Redmi Note 12, 38000.0руб. Остаток: 44шт.\n"
    )


def test_add_product(test_category_data):
    product1 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 30000.0, 14)
    test_category_data.add_product(product1)
    assert test_category_data.products == (
        "Xiaomi Redmi Note 11, 31000.0руб. Остаток: 15шт.\n"
        "Xiaomi Redmi Note 12, 38000.0руб. Остаток: 44шт.\n"
        "Xiaomi Redmi Note 11, 30000.0руб. Остаток: 14шт.\n"
    )


def test_products_list(test_category_data):
    assert test_category_data.products_list[0].name == "Xiaomi Redmi Note 11"


def test_add_product_error(test_category_data):
    with pytest.raises(TypeError):
        test_category_data.add_product("Not a product")
