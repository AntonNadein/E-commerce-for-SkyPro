from src.base_category import BaseCategory
from src.product import Product


class Order(BaseCategory, Product):
    """Класс выводящий информацию о заказе"""

    def __init__(self, name: str, price: float, quantity: int, description=None) -> None:
        super().__init__(name, description, price, quantity)
        self.cost = self.price * self.quantity

    def __str__(self):
        """Вывод информации для пользователлей"""
        return f"Заказ: {self.name}\n" f"количество:{self.quantity}\n" f"итоговая стоимость: {self.cost} руб."

    # def __add__(self, other):
    #     pass


# if __name__ == '__main__':
#     # product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 170000.0, 1)
#
#     order_2 = Order("Samsung Galaxy S23 Ultra", 150000.0, 2)
#     print(order_2)
#     # print(product1+order_2)
