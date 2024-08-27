import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def test_product_data():
    return Product("test", "test_description", 50.50, 5)


@pytest.fixture()
def test_category_data():
    product_1 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 15)
    product_2 = Product("Xiaomi Redmi Note 12", "1024GB, Синий", 38000.0, 44)
    return Category("test_category", "test_description", [product_1, product_2])


@pytest.fixture()
def test_second_category_data():
    return Category("test_second", "test_description")


@pytest.fixture()
def test_category_to_list_data():
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфон - удобство жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
            ],
        }
    ]


@pytest.fixture()
def test_product_1_add():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 15)


@pytest.fixture()
def test_product_2_add():
    return Product("Xiaomi Redmi Note 12", "1024GB, Синий", 38000.0, 44)
