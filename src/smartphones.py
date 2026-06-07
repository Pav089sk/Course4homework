from src.products import Product

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            first_prod = self.quantity * self.price
            second_prod = other.quantity * other.price
            return first_prod + second_prod
        raise TypeError


# if __name__ == "__main__":
#     product1 = Smartphone('Iphone 17', 'Apple smartphone', 65000, 1, 'A19', "A2111", "256GB", "white")
#     product2 = Smartphone('Iphone 16', 'Apple smartphone', 50000, 2, 'A18', "A2100", "128GB", "black")
#     product3 = Product('Лук', 'Овощи', 8.50, 5)
#
#     print(product1 + product2)
#     product1 + product3