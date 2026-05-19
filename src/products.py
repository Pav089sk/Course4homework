

class Product:
    """Класс описания продукта"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

if __name__ == '__main__':
    product1 = Product('Яблоко', 'Фрукты', 18.40, 5)
    product2 = Product('Груша', 'Фрукты', 13.60, 5)
    product3 = Product('Лук', 'Овощи', 8.50, 5)
    product4 = Product('Помидор', 'Овощи', 12.8, 5)

    print(product1.description)
    print(product2.price)
    print(product4.quantity)
