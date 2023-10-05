import pytest

from src.item import Item
from pathlib import Path
from src.phone import Phone

path = Path.cwd().parent.joinpath('src/items.csv')

@pytest.fixture
def item1():
    return Item("Товар 1", 20, 10)

@pytest.fixture
def item2():
    return Item('Товар 2', 10, 10)

@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)

def test_calculate_total_price(item1, item2):
    assert item1.calculate_total_price() == 200
    assert item2.calculate_total_price() == 100

def test_apply_discount(item1, item2):
    Item.pay_rate = 0.9
    item1.apply_discount()

    assert item1.price == 18
    assert item2.price == 10

    item2.apply_discount()
    assert item2.price == 9

def test_string_to_number(item1, item2):
    assert item1.string_to_number('10') == 10
    assert item2.string_to_number('10.99') == 10

def test_instantiate_from_csv(item1, item2):
    item1.instantiate_from_csv(path)
    assert len(item1.all) == 5
    assert len(item2.all) == 5

    item2.instantiate_from_csv(path)
    assert len(item2.all) == 10

def test_item_repr_and_str(item1, item2):
    assert repr(item1) == "Item('Товар 1', 20, 10)"
    assert repr(item2) == "Item('Товар 2', 10, 10)"
    assert str(item1) == 'Товар 1'
    assert str(item2) == 'Товар 2'

def tests_phone_repr_and_str(item1, phone1):
    assert repr(item1) == "Item('Товар 1', 20, 10)"
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert str(item1) == 'Товар 1'
    assert str(phone1) == 'iPhone 14'

def tests_phone_add(item1,phone1):
    assert phone1 + item1 == 15
    assert phone1 + phone1 == 10