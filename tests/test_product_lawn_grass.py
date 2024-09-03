import pytest


def test_product_lawn_grass(test_product_lawn_grass_1):
    assert (test_product_lawn_grass_1.name) == "Газон"
    assert (test_product_lawn_grass_1.description) == "Полевая трава"
    assert (test_product_lawn_grass_1.price) == 250
    assert (test_product_lawn_grass_1.quantity) == 20
    assert (test_product_lawn_grass_1.country) == "Россия"
    assert (test_product_lawn_grass_1.germination_period) == "5 дней"
    assert (test_product_lawn_grass_1.color) == "зеленый"


def test_product_lawn_grass_add(test_product_lawn_grass_1, test_product_lawn_grass_2):
    result = test_product_lawn_grass_1 + test_product_lawn_grass_2
    assert result == 520


def test_product_lawn_grass_add_error(test_product_lawn_grass_1):
    with pytest.raises(TypeError):
        print(test_product_lawn_grass_1 + 100)
