
def test_all_prod(fruits_vegetables, smartphones):
    assert fruits_vegetables.name == "Фрукты и овощи"
    assert fruits_vegetables.description == "Все сладкое и вкусное"
    assert smartphones.name == "Смартфоны"
    assert smartphones.description == "Современные средства связи"
    assert fruits_vegetables.product_count == 6
    assert fruits_vegetables.category_count == 2
    assert smartphones.product_count == 6
    assert smartphones.category_count == 2


def test_party_prod(drinks, snacks):
    assert drinks.name == "Напитки"
    assert drinks.description == "Сладкие газированные напитки"
    assert snacks.name == "Снэки"
    assert snacks.description == "Любые хрустящие закуски"
    assert drinks.product_count == 5
    assert drinks.category_count == 2
    assert snacks.product_count == 5
    assert snacks.category_count == 2


def test_add_product(unit_product, cat_for_test):
    cat_for_test.add_product(unit_product)
    counter = cat_for_test.product_count
    assert counter == 1
    assert unit_product in cat_for_test._Category__products


def test_add_no_product(cat_for_test):
    cat_for_test.add_product("Не продукт")
    counter = cat_for_test.product_count
    assert counter == 0
    assert "Объект не является продуктом"
