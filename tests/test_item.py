from src.item import Item
from pathlib import Path

path = Path.cwd().parent.joinpath('src/items.csv')

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

def test_string_to_number():
    assert item1.string_to_number('10') == 10
    assert item2.string_to_number('10.99') == 10

def test_instantiate_from_csv():
    item1.instantiate_from_csv(path)
    assert len(item1.all) == 5
    assert len(item2.all) == 5

    item2.instantiate_from_csv(path)
    assert len(item2.all) == 10
