from src.item import Item

item1 = Item("Товар 1", 20, 10)
item2 = Item('Товар 2', 10, 10)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200
    assert item2.calculate_total_price() == 100

def test_apply_discount():
    Item.pay_rate = 0.9
    item1.apply_discount()

    assert item1.price == 18
    assert item2.price == 10

    item2.apply_discount()
    assert item2.price == 9

def test_all():
    assert len(Item.all) == 2
    item3 = Item('Товар 3', 5, 10)
    assert len(Item.all) == 3

