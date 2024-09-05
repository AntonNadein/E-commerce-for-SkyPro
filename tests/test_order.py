from src.order import Order


def test_order(capsys):
    order = Order("Samsung Galaxy S23 Ultra", 150000.0, 2)
    assert str(order) == "Заказ: Samsung Galaxy S23 Ultra\nколичество:2\nитоговая стоимость: 300000.0 руб."
