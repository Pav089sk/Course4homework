import pytest

def test_smartphone_1(smartphone1):
    assert smartphone1.name == 'Iphone 17'
    assert smartphone1.model == 'A2111'
    assert smartphone1.memory == '256GB'
    assert smartphone1.color == 'White'

def test_smartphones_add(smartphone1, smartphone2):
    assert smartphone1 + smartphone2 == 165000

def test_add_error(smartphone1, prod_data):
    with pytest.raises(TypeError):
        res = smartphone1 + prod_data
