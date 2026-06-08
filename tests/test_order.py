from src.order import Order


def test_order(smartphone1):
    order = Order(smartphone1, 2, "Заказ-001")
    assert order.name == "Заказ-001"
