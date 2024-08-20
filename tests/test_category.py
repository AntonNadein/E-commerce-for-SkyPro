from src.category import Category


def test_category(test_category_data, test_second_category_data):
    assert test_category_data.name == "test_category"
    assert test_category_data.description == "test_description"
    assert len(test_category_data.products) == 2
    assert Category.product_count == 2
    assert Category.category_count == 2
