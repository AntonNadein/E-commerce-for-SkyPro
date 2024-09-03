import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.product import Product
from src.product_lawn_grass import LawnGrass
from src.product_smartphone import Smartphone


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


@pytest.fixture()
def test_category_iterator_data():
    product_1 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 15)
    product_2 = Product("Xiaomi Redmi Note 12", "1024GB, Синий", 38000.0, 44)
    category = Category("test_category", "test_description", [product_1, product_2])
    return CategoryIterator(category)

@pytest.fixture()
def test_product_lawn_grass_1():
    return LawnGrass("Газон", "Полевая трава", 250, 20, "Россия", "5 дней", "зеленый")


@pytest.fixture()
def test_product_lawn_grass_2():
    return LawnGrass("Газон", "Полевая трава", 270, 20, "Россия", "7 дней", "зеленый")


@pytest.fixture()
def test_product_smartphone_1():
    return Smartphone("Redmi", "Смартфон Redmi", 25000, 20, 23.3, "Note 7", 60, "черный")


@pytest.fixture()
def test_product_smartphone_2():
    return Smartphone("Redmi", "Смартфон Redmi", 33000, 10, 55.6, "Note 8", 120, "черный")
