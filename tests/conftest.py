import pytest

from src.categories import Category
from src.products import Product
from src.iteration import IterProducts

@pytest.fixture(autouse=True)
def reset_category_counts():
    Category.category_count = 0
    Category.product_count = 0


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


@pytest.fixture(autouse=True)
def iphone():
    return Product("Iphone 17", "Последняя модель Apple IPhone", 68000, 4)


@pytest.fixture(autouse=True)
def fruit():
    return Product("Яблоко", "Фрукты сладкие", 18.40, 5)


@pytest.fixture(autouse=True)
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


@pytest.fixture
def drinks():
    return Category(
        name="Напитки",
        description="Сладкие газированные напитки",
        products=[
            Product("Кола", "Добрый Кола", 129, 10),
            Product("RedBull", "Энергетический напиток", 179, 8),
        ],
    )


@pytest.fixture
def snacks():
    return Category(
        name="Снэки",
        description="Любые хрустящие закуски",
        products=[
            Product("Чипсы Lays", "Чипсы Lays классические с солью", 159, 7),
            Product("Чипсы Pringles", "Чипсы Pringles с вкусом паприки", 179, 8),
            Product("Чипсы Naturals", "Чипсы Naturals с вкусом пармезана", 119, 11),
        ],
    )


@pytest.fixture
def unit_product():
    return Product("Тестовый продукт", "Тестовое описание", 100, 50)

@pytest.fixture
def unit_product2():
    return Product("Тестовый продукт2", "Тестовое описание2", 100, 20)

@pytest.fixture
def cat_for_test():
    return Category("Тестовая категория", "Описание", [])


@pytest.fixture
def prod_data():
    data = {"name": "Груша", "description": "Фрукты сладкие", "price": 13.60, "quantity": 5}
    return data


@pytest.fixture
def update_data():
    data2 = {"name": "Груша", "description": "Фрукты сладкие", "price": 90.60, "quantity": 14}
    return data2


@pytest.fixture
def products_iterator(smartphones):
    return IterProducts(smartphones)