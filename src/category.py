from src.base_category import BaseCategory
from src.exceptions import ZeroQuantityProduct
from src.product import Product


class Category(BaseCategory):
    """Класс для представления категорий продукта."""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None) -> None:
        """Инициализация характеристик категорий продукта."""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        """Вывод информации для пользователлей"""
        count_quantity = 0
        for i in self.__products:
            count_quantity += i.quantity
        return f"{self.name}, количество продуктов: {count_quantity} шт."

    @property
    def products(self):
        """Вывод приватного атрибута products"""
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    def add_product(self, new_product: Product):
        """Добавление приватного атрибута products"""
        if isinstance(new_product, Product):
            try:
                if new_product.quantity == 0:
                    raise ZeroQuantityProduct("Передан пустой список")
            except ZeroQuantityProduct as e:
                print(e)
            else:
                self.__products.append(new_product)
                print("Товар добавлен")
                Category.product_count += 1
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError

    def middle_price(self):
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0

    @property
    def products_list(self):
        """Вывод всего списка products"""
        return self.__products


# if __name__ == "__main__":
#     product_1 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 30000.0, 10)
#     product_2 = Product("Xiaomi Redmi Note 12", "1024GB, Синий", 38000.0, 10)
#     category = Category("test_category", "test_description", [product_1, product_2])
#     product_3 = Product("Xiaomi Redmi Note 13", "1024GB, Синий", 38000.0, 5)
#     product_3.quantity = 0
#     category.add_product(product_3)
#
#     print(category.products)
