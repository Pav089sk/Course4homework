from products import Product


class Category:
    """Класс категории продукта"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        """Инициализация класса категории продукта"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)


    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            print('Объект не является продуктом')

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return product_str




# if __name__ == '__main__':
#     # pragma: no cover
#     product1 = Product('Яблоко', 'Фрукты сладкие', 18.40, 5)
#     product2 = Product('Груша', 'Фрукты сладкие', 13.60, 5)
#     product3 = Product('Лук', 'Овощи', 8.50, 5)
#     product4 = Product('Помидор', 'Овощи', 12.8, 5)
#     category1 = Category('Фрукты', 'Все сладкое и вкусное', [product1, product2, product3])
#     print(category1.name)
#     print(category1.products)
#     print(category1.category_count)
#     print(category1.product_count)


