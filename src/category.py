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

    @property
    def products(self):
        """Вывод приватного атрибута products"""
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price}руб. Остаток: {product.quantity}шт.\n"
        return product_str

    def add_product(self, new_product: Product):
        """Добавление приватного атрибута products"""
        for product in self.__products:
            if product.name == new_product.name:
                product.quantity += new_product.quantity
                if product.price < new_product.price:
                    product.price = new_product.price
                return
            else:
                self.__products.append(new_product)
                Category.product_count += 1
                return self.__products
