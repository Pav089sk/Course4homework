import pytest


def test_lawn_grass_1(lawn_grass1):
    assert lawn_grass1.name == "Gazon"
    assert lawn_grass1.country == "Russia"
    assert lawn_grass1.germination_period == "50"
    assert lawn_grass1.color == "Green"


def test_lawn_grass_add(lawn_grass1, lawn_grass2):
    assert lawn_grass1 + lawn_grass2 == 160000


def test_add_error(lawn_grass1, prod_data):
    with pytest.raises(TypeError):
        res = lawn_grass1 + prod_data
