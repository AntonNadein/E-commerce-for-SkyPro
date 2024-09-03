from src.product import Product


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.price + other.price
        else:
            raise TypeError


# if __name__ == "__main__":
# grass_1 = LawnGrass("Газон", "Полевая трава", 250, 20, "Россия", "5 дней", "зеленый")
# grass_2 = LawnGrass("Газон", "Полевая трава", 270, 20, "Россия", "7 дней", "зеленый")
# print(grass_1.name)
# print(grass_1.description)
# print(grass_1.price)
# print(grass_1.quantity)
# print(grass_1.country)
# print(grass_1.germination_period)
# print(grass_1.color)
# print(grass_1 + grass_2)
