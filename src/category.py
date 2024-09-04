from src.product import Product


class Category:
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
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products_list(self):
        """Вывод всего списка products"""
        return self.__products
