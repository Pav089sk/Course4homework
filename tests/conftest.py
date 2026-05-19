import pytest

from src.categories import Category
from src.products import Product


@pytest.fixture
def fruits_vegetables():
    return Category(
        name="Фрукты и овощи",
        description="Все сладкое и вкусное",
        products=[
            Product("Яблоко", "Фрукты сладкие", 18.40, 5),
            Product("Груша", "Фрукты сладкие", 13.60, 5),
            Product("Помидор", "Овощи", 12.8, 5),
        ],
    )


@pytest.fixture
def smartphones():
    return Category(
        name="Смартфоны",
        description="Современные средства связи",
        products=[
            Product("Iphone 17", "Последняя модель Apple IPhone", 68000, 4),
            Product("Samsung Galaxy S26", "Последняя модель Samsung", 65890, 3),
            Product("Huawei Mate70", "Одна из моделей линейки Huawei", 50299, 5),
        ],
    )


@pytest.fixture
def iphone():
    return Product("Iphone 17", "Последняя модель Apple IPhone", 68000, 4)


@pytest.fixture
def fruit():
    return Product("Яблоко", "Фрукты сладкие", 18.40, 5)


@pytest.fixture
def data_for_test():
    return [
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        }
    ]
