from unittest.mock import patch

import pytest

from src.products import Product


def test_iphone_init(iphone):
    assert iphone.name == "Iphone 17"
    assert iphone.description == "Последняя модель Apple IPhone"
    assert iphone.price == 68000
    assert iphone.quantity == 4


def test_fruit_init(fruit):
    assert fruit.name == "Яблоко"
    assert fruit.description == "Фрукты сладкие"
    assert fruit.price == 18.40
    assert fruit.quantity == 5


def test_clas(prod_data):
    new_prod = Product.new_product(prod_data)
    assert new_prod.name == "Груша"


def test_clas_2(prod_data, update_data):
    existing_prod = Product("Груша", "Фрукты сладкие", 13.60, 5)
    products_list = [existing_prod]
    updated_prod = Product.new_product(update_data, products_list)
    assert updated_prod is existing_prod  # тот же объект
    assert updated_prod.price == 90.60  # максимальная цена
    assert updated_prod.quantity == 19  # 5 + 14 = 19
    assert len(products_list) == 1


@patch("builtins.input", return_value="y")
def test_price(mock_input):
    product = Product("Телефон", "Дорогой", 100000, 5)
    product.price = 800
    assert product.price == 800
    mock_input.assert_called_once_with("Подтвердите понижение цены: 'y' — Да, 'n' — Нет: ")


@patch("builtins.input", return_value="n")
def test_price_no(mock_input):
    product = Product("Телефон", "Дорогой", 100000, 5)
    product.price = 800
    assert product.price == 100000
    mock_input.assert_called_once_with("Подтвердите понижение цены: 'y' — Да, 'n' — Нет: ")


def test_price_emp():
    product = Product("Телефон", "Дорогой", 100000, 5)
    product.price = -100
    assert product.price == 100000
    assert "Цена не должна быть нулевая или отрицательная"


def test_product_add(unit_product, unit_product2):
    assert unit_product + unit_product2 == 7000

def test_add_error_prod(unit_product):
    with pytest.raises(TypeError):
        res = unit_product + 1

def test_iter_products(products_iterator):
    iter(products_iterator)
    assert products_iterator.start == 0
    assert next(products_iterator).name == "Iphone 17"
    assert next(products_iterator).name == "Samsung Galaxy S26"
    assert next(products_iterator).name == "Huawei Mate70"
    with pytest.raises(StopIteration):
        next(products_iterator)

