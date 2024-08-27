class Product:
    """Класс для представления продукта."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация характеристик продукта."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price}руб. Остаток: {self.quantity}шт."

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, product_dict: dict):
        """Добавление нового продукта через класс-метод"""
        name = product_dict["name"]
        description = product_dict["description"]
        price = product_dict["price"]
        quantity = product_dict["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Вывод приватного атрибута price"""
        return self.__price

    @price.setter
    def price(self, value: float):
        """Добавление/изменение приватного атрибута price"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            answer = input("Вы уверены что хотите изменить цену товара введите 'yes'")
            if answer == "yes":
                self.__price = value
        else:
            self.__price = value


# product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 1)
# product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 2)
# product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
# print(product1)
# print(product2)
# print(product3)
#
# print(product1+product2)
