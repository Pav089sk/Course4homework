from src.products import Product
from src.baseabs import Named


class Order(Named):

    def __init__(self, product: Product, quantity: int, order_id: str = None):
        self.product = product
        self.quantity = quantity
        self.cost = product.price * quantity
        self._name = order_id or f"Заказ №{id(self)}"

    @property
    def name(self) -> str:  # реализуем абстрактное свойство
        return self._name



# if __name__ == '__main__':
#     p = Product("Ноутбук", "Мощный", 50000, 10)
#
#     order = Order(p, 2, "Заказ-001")
#     cat = Category("Электроника", "Всё для ПК")
#
#     print(order.name)   # Заказ-001
#     print(cat.name)