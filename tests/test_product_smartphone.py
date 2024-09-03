import pytest


def test_product_smartphone(test_product_smartphone_1, test_product_smartphone_2):
    assert (test_product_smartphone_1.name) == "Redmi"
    assert (test_product_smartphone_1.description) == "Смартфон Redmi"
    assert (test_product_smartphone_1.price) == 25000
    assert (test_product_smartphone_1.quantity) == 20
    assert (test_product_smartphone_1.efficiency) == 23.3
    assert (test_product_smartphone_1.model) == "Note 7"
    assert (test_product_smartphone_1.memory) == 60
    assert (test_product_smartphone_1.color) == "черный"


def test_product_smartphone_add(test_product_smartphone_1, test_product_smartphone_2):
    result = test_product_smartphone_1 + test_product_smartphone_2
    assert result == 58000


def test_product_smartphone_add_error(test_product_smartphone_1):
    with pytest.raises(TypeError):
        print(test_product_smartphone_1 + 100)
