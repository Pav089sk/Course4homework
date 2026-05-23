def test_all_prod(fruits_vegetables, smartphones):
    assert fruits_vegetables.name == "Фрукты и овощи"
    assert fruits_vegetables.description == "Все сладкое и вкусное"
    assert len(fruits_vegetables.products) == 3
    assert smartphones.name == "Смартфоны"
    assert smartphones.description == "Современные средства связи"
    assert len(smartphones.products) == 3
    assert fruits_vegetables.product_count == 6
    assert fruits_vegetables.category_count == 2
    assert smartphones.product_count == 6
    assert smartphones.category_count == 2


def test_party_prod(drinks, snacks):
    assert drinks.name == "Напитки"
    assert drinks.description == "Сладкие газированные напитик"
    assert len(drinks.products) == 2
    assert snacks.name == "Снэки"
    assert snacks.description == "Любые хрустящие закуски"
    assert len(snacks.products) == 3
    assert drinks.product_count == 5
    assert drinks.category_count == 2
    assert snacks.product_count == 5
    assert snacks.category_count == 2
