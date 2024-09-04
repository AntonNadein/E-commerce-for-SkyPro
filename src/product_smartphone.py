from src.product import Product


class Smartphone(Product):
    """Подкласс продукта «Смартфон»"""

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Сложение товаров только из одиного класса продукта"""
        if type(other) is Smartphone:
            return self.price + other.price
        else:
            raise TypeError


# if __name__ == "__main__":
#     smart_1 = Smartphone("Redmi", "Смартфон Redmi", 250, 20, 23.3, "Note 7", 60, "черный")
#     smart_2 = Smartphone("Redmi", "Смартфон Redmi", 250, 20, 55.6, "Note 7", 60, "черный")
#     print(smart_1.name)
#     print(smart_1.description)
#     print(smart_1.price)
#     print(smart_1.quantity)
#     print(smart_1.efficiency)
#     print(smart_1.model)
#     print(smart_1.memory)
#     print(smart_1.color)
#     print(smart_1 + 100)
