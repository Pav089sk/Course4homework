from src.products import Product


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            first_prod = self.quantity * self.price
            second_prod = other.quantity * other.price
            return first_prod + second_prod
        raise TypeError


# if __name__ == "__main__":
#     product = LawnGrass('Gazon', 'grass for garden', 5000, 10, 'Russia', "50", "green")
#     product2 = LawnGrass('NewGazon', 'best grass for garden', 10000, 11, 'Belarus', "25", "royal green")
#     product3 = Product('Лук', 'Овощи', 8.50, 5)
#
#     print(product + product2)
#     product + product3
