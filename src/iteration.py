class IterProducts:
    """Вспомогательный класс, с помощью которого можно перебирать товары одной категории"""

    def __init__(self, cat_obj):
        self.category = cat_obj
        self.start = 0

    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):
        if self.start < len(self.category.product_list):
            prod = self.category.product_list[self.start]
            self.start += 1
            return prod
        else:
            raise StopIteration


# if __name__ == '__main__':
#     product1 = Product('Яблоко', 'Фрукты сладкие', 18.40, 9)
#     product2 = Product('Груша', 'Фрукты сладкие', 13.60, 5)
#     product3 = Product('Лук', 'Овощи', 8.50, 15)
#     product4 = Product('Помидор', 'Овощи', 12.8, 5)
#     category1 = Category('Еда', 'Фрукты и овощи', [product1, product2, product3, product4])
#
#     iterator = IterProducts(category1)
#
#     for product in iterator:
#         print(product)
