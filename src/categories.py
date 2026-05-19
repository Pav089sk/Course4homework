from unicodedata import category

from src.products import Product

class Category:
    """Класс категории продукта"""
    name: str
    description: str
    products: list
    quantity_categories = 0
    quantity_products = 0


    def __init__(self, name,description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.quantity_categories += 1
        Category.quantity_products = len(products) if products else 0


if __name__ == '__main__':
    product1 = Product('Яблоко', 'Фрукты', 18.40, 5)
    product2 = Product('Груша', 'Фрукты', 13.60, 5)
    product3 = Product('Лук', 'Овощи', 8.50, 5)
    product4 = Product('Помидор', 'Овощи', 12.8, 5)

    category1 = Category('Фрукты', 'Все сладкое и вкусное', [product1, product2])

    print(category1.name)
    print(category1.products)
    print(category1.quantity_products)
    print(category1.quantity_categories)