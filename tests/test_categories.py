


def test_all_prod(fruits_vegetables, smartphones):
    assert fruits_vegetables.name == 'Фрукты и овощи'
    assert fruits_vegetables.description == 'Все сладкое и вкусное'
    assert len(fruits_vegetables.products) == 3
    assert smartphones.name == 'Смартфоны'
    assert smartphones.description == 'Современные средства связи'
    assert len(smartphones.products) == 3
    assert fruits_vegetables.quantity_products == 3
    assert fruits_vegetables.quantity_categories == 2
    assert smartphones.quantity_products == 3
    assert smartphones.quantity_categories == 2
