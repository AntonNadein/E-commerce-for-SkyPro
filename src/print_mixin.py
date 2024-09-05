class PrintMixin:

    def __init__(self):
        self.__repr__()
        # print(repr(self))

    def __repr__(self, *args, **kwargs):
        print(f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})")
        # return f'{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})'
