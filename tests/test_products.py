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
