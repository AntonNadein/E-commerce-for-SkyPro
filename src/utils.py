import os
import json

from src.category import Category
from src.product import Product


def open_json(file: str) -> dict:
    with open(os.path.abspath(file), "r", encoding="UTF-8") as f:
        return json.load(f)


def category_to_list(data: dict) -> list:
    result_list = []
    for category in data:
        list_product = []
        for product in category["products"]:
            list_product.append(Product(**product))
        category["products"] = list_product
        result_list.append(Category(**category))
    return result_list
