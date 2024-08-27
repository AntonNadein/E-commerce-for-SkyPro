from src.product import Product


class Category:
    """Класс для представления категорий продукта."""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        """Инициализация характеристик категорий продукта."""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        return f"{self.name}, количество продуктов: {Category.product_count} шт."

    @property
    def products(self):
        """Вывод приватного атрибута products"""
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    def add_product(self, new_product: Product):
        """Добавление приватного атрибута products"""
        self.__products.append(new_product)
        Category.product_count += 1


#
# product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
# product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
# product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
# category1 = Category(
#     "Смартфоны",
#     "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#     [product1, product2, product3])
#
# print(category1)
# print(category1.products)
#
# product4 = Product("Xiaomi Redmi Note 12", "1024GB, Синий", 31000.0, 14)
# category1.add_product(product4)
#
# print(category1)
# print(category1.products)
