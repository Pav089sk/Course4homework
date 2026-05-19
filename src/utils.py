import json
import os
from src.products import Product
from src.categories import Category

def read_json_data(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding="UTF-8") as file:
        data = json.load(file)
        return data

def creator_from_json(data):
    categories = []
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product(**product))
        categories.append(Category(**category))
    return categories


# if __name__ == '__main__':
#
#     print(read_json_data('../data/products.json'))
#     print(creator_from_json(read_json_data('../data/products.json')))
#     print(creator_from_json(read_json_data('../data/products.json'))[0].name)
#     print(creator_from_json(read_json_data('../data/products.json'))[0].products)