from src.baseabs import BaseProduct
from src.mixinclass import MixinStr


class Product(BaseProduct, MixinStr):
    """Класс описания продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация класса описания продукта"""
        self.name = name
        self.description = description
        self.__price = price
        if quantity == 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        else:
            self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            first_prod = self.quantity * self.price
            second_prod = other.quantity * other.price
            return first_prod + second_prod
        raise TypeError

    @classmethod
    def new_product(cls, product_data: dict, products_list=None):
        if products_list is None:
            products_list = []
        for prod in products_list:
            if prod.name == product_data["name"]:
                new_quantity = prod.quantity + product_data["quantity"]
                new_price = max(prod.price, product_data["price"])
                prod.quantity = new_quantity
                prod.price = new_price
                return prod
        new_product = cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )
        return new_product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            answer = input("Подтвердите понижение цены: 'y' — Да, 'n' — Нет: ").strip().lower()
            if answer == "y":
                self.__price = new_price
            else:
                print("Изменение цены отменено.")
        else:
            self.__price = new_price


if __name__ == '__main__':
#     # pragma: no cover
    product1 = Product('Яблоко', 'Фрукты сладкие', 10, 10)
#     product2 = Product('Груша', 'Фрукты сладкие', 20, 5)
#     product3 = Product('Лук', 'Овощи', 8.50, 5)
#     product4 = Product('Помидор', 'Овощи', 0, 5)
# #     print(product1 + product2)


#     #     print(product1.description)
#     #     print(product3.price)
#     #     print(product4.quantity)
#     print(f"Начальная цена: {product1.price} руб.")  # Геттер
#     # Меняем цену на корректную
#     product1.price = 20.00
#     print(f"Новая цена: {product1.price} руб.")  # Геттер после изменения
#     # Попытка установить нулевую цену
#     print("Попытка установить цену = 0:")
#     product1.price = 0  # Сеттер с некорректным значением
#     print(f"Цена после попытки: {product1.price} руб.")
#     # Попытка установить отрицательную цену
#     print("Попытка установить цену = -5:")
#     product1.price = -5  # Сеттер с некорректным значением
#     print(f"Цена после попытки: {product1.price} руб.")

# Создаём продукт через classmethod
#     data = {
#     'name': 'Груша',
#     'description': 'Фрукты сладкие',
#     'price': 13.60,
#     'quantity': 5
#     }
#     product2 = Product.new_product(data)
#     print(product2)
# print(f"\nПродукт из new_product: {product2.name}, {product2.description},  цена: {product2.price} руб, {product2.quantity} шт.")
