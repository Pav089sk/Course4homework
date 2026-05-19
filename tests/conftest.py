import pytest

from src.products import Product
from src.categories import Category

@pytest.fixture
def fruits_vegetables():
    return Category(
        name='Фрукты и овощи',
        description='Все сладкое и вкусное',
        products=[Product('Яблоко', 'Фрукты сладкие', 18.40, 5),
                  Product('Груша', 'Фрукты сладкие', 13.60, 5),
                  Product('Помидор', 'Овощи', 12.8, 5)
        ]
    )

@pytest.fixture
def smartphones():
    return Category(
        name='Смартфоны',
        description='Современные средства связи',
        products=[Product('Iphone 17', 'Последняя модель Apple IPhone', 68000, 4),
                  Product('Samsung Galaxy S26', 'Последняя модель Samsung', 65890, 3),
                  Product('Huawei Mate70', 'Одна из моделей линейки Huawei', 50299, 5)
        ]
    )

@pytest.fixture
def iphone():
    return Product('Iphone 17', 'Последняя модель Apple IPhone', 68000, 4)

@pytest.fixture
def fruit():
    return Product('Яблоко', 'Фрукты сладкие', 18.40, 5)