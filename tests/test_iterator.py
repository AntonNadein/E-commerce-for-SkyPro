import pytest


def test_category_iterator(test_category_iterator_data):
    iter(test_category_iterator_data)
    assert test_category_iterator_data.start == 0
    assert next(test_category_iterator_data).name == "Xiaomi Redmi Note 11"
    assert next(test_category_iterator_data).name == "Xiaomi Redmi Note 12"
    with pytest.raises(StopIteration):
        next(test_category_iterator_data)
