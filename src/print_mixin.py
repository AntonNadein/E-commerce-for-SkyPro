class PrintMixin:

    def __init__(self):
        print(repr(self))

    def __repr__(self, *args, **kwargs):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
