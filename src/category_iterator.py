class CategoryIterator:
    """Класс для итерации в классе категории по продукту"""

    def __init__(self, user_object):
        self.category = user_object
        self.start = 0

    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):
        if self.start < len(self.category.products_list):
            product = self.category.products_list[self.start]
            self.start += 1
            return product
        else:
            raise StopIteration
