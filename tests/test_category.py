from src.category import Category
from src.product import Product


def test_category(test_category_data, test_second_category_data):
    assert test_category_data.name == "test_category"
    assert test_category_data.description == "test_description"
    assert Category.product_count == 2
    assert Category.category_count == 2


def test_products_property(test_category_data):
    assert test_category_data.products == (
        "Xiaomi Redmi Note 11, 31000.0руб. Остаток: 15шт.\n" "Xiaomi Redmi Note 12, 38000.0руб. Остаток: 44шт.\n"
    )


def test_add_product(test_category_data):
    product1 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 30000.0, 14)
    test_category_data.add_product(product1)
    assert test_category_data.products == (
        "Xiaomi Redmi Note 11, 31000.0руб. Остаток: 29шт.\n" "Xiaomi Redmi Note 12, 38000.0руб. Остаток: 44шт.\n"
    )
    product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 33000.0, 11)
    test_category_data.add_product(product2)
    assert test_category_data.products == (
        "Xiaomi Redmi Note 11, 33000.0руб. Остаток: 40шт.\n" "Xiaomi Redmi Note 12, 38000.0руб. Остаток: 44шт.\n"
    )
    product3 = Product("Xiaomi Redmi Note 13", "2048GB, Синий", 44000.0, 40)
    test_category_data.add_product(product3)
    assert test_category_data.products == (
        "Xiaomi Redmi Note 11, 33000.0руб. Остаток: 40шт.\n"
        "Xiaomi Redmi Note 12, 38000.0руб. Остаток: 44шт.\n"
        "Xiaomi Redmi Note 13, 44000.0руб. Остаток: 40шт.\n"
    )
