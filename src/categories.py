from src.baseabs import Named
from src.products import Product


class Category(Named):
    """Класс категории продукта"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        """Инициализация класса категории продукта"""
        self._name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def name(self) -> str:  # реализуем абстрактное свойство
        return self._name

    def __str__(self):
        quantity = 0
        for product in self.__products:
            quantity += product.quantity
        return f"{self.name}, количество продуктов: {quantity}."

    def add_product(self, product):
        """Метод добавляет продукт в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            print("Объект не является продуктом")

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def product_list(self):
        return self.__products

    @property
    def middle_price(self):
        try:
            avg_price = sum(p.price for p in self.__products) / len(self.__products)
            return round(avg_price, 2)
        except:
            if len(self.__products) == 0:
                return 0


if __name__ == '__main__':
#     # pragma: no cover
    product1 = Product('Яблоко', 'Фрукты сладкие', 18.40, 9)
    product2 = Product('Груша', 'Фрукты сладкие', 13.60, 5)
    product3 = Product('Лук', 'Овощи', 8.50, 15)
    product4 = Product('Помидор', 'Овощи', 12.8, 5)
    category1 = Category('Фрукты', 'Все сладкое и вкусное', [product1, product2, product3, product4])
#     print(category1.name)
#     print(category1.products)
#     print(category1.category_count)
#     print(category1.product_count)
#     print(str(category1))
    print(category1.middle_price)
