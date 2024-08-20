def test_product(test_product_data):
    assert test_product_data.name == "test"
    assert test_product_data.description == "test_description"
    assert test_product_data.price == 50.50
    assert test_product_data.quantity == 5
