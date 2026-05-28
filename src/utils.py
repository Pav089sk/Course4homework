import json
import os

from src.categories import Category
from src.products import Product


def read_json_data(path: str) -> dict:
    """Функция для получения данных из JSON файла"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
        return data


def creator_from_json(data):
    """Функция для приведения данных к классам"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category = Category(name=category["name"], description=category["description"], products=products)
        categories.append(category)
    return categories


# if __name__ == '__main__':

# print(read_json_data('../data/products.json'))
# print(creator_from_json(read_json_data('../data/products.json')))
# print(creator_from_json(read_json_data('../data/products.json'))[0].name)
#   print(creator_from_json(read_json_data('../data/products.json'))[0].products)
