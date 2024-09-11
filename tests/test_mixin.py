from src.product import Product
from src.product_lawn_grass import LawnGrass
from src.product_smartphone import Smartphone


def test_print_mixin(capsys):
    Product("Redmi", "Смартфон Redmi", 250, 20)
    result = capsys.readouterr()
    assert result.out.strip() == "Product(Redmi, Смартфон Redmi, 250, 20)"

    Smartphone("Redmi", "Смартфон Redmi", 250, 20, 23.3, "Note 7", 60, "черный")
    result = capsys.readouterr()
    assert result.out.strip() == "Smartphone(Redmi, Смартфон Redmi, 250, 20)"

    LawnGrass("Газон", "Полевая трава", 300, 50, "Россия", "5 дней", "зеленый")
    result = capsys.readouterr()
    assert result.out.strip() == "LawnGrass(Газон, Полевая трава, 300, 50)"
