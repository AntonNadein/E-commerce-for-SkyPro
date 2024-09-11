import pytest

from src.category import Category
from src.exceptions import ZeroQuantityProduct
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


def test_get_average_price_product(test_category_data):
    result = test_category_data.middle_price()
    assert result == 34500.0


def test_get_average_price_product_div_0(test_category_data):
    result = Category("test_category", "test_description", [])
    assert result.middle_price() == 0


def test_category_product_quantity_0(capsys):
    product_2 = Product("Xiaomi Redmi Note 12", "1024GB, Синий", 38000.0, 10)
    category = Category("test_category", "test_description", [product_2])
    product_3 = Product("Xiaomi Redmi Note 13", "1024GB, Синий", 38000.0, 5)
    product_3.quantity = 0
    category.add_product(product_3)
    result = capsys.readouterr()
    assert str(result.out.split("\n")[-2]) == "Обработка добавления товара завершена"
    assert str(result.out.split("\n")[-3]) == "Передан пустой список"


def test_category_product_quantity(capsys):
    Category.product_count = 0
    product_2 = Product("Xiaomi Redmi Note 12", "1024GB, Синий", 38000.0, 10)
    category = Category("test_category", "test_description", [product_2])
    product_3 = Product("Xiaomi Redmi Note 13", "1024GB, Синий", 38000.0, 5)
    category.add_product(product_3)
    result = capsys.readouterr()
    assert str(result.out.split("\n")[-2]) == "Обработка добавления товара завершена"
    assert str(result.out.split("\n")[-3]) == "Товар добавлен"
    assert Category.product_count == 2
