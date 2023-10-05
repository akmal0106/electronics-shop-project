import pytest

from src.item import Item
from src.phone import Phone

@pytest.fixture
def item1():
    return Item("Товар 1", 20, 10)

@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


def tests_repr_and_str(item1, phone1):
    assert repr(item1) == "Item('Товар 1', 20, 10)"
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert str(item1) == 'Товар 1'
    assert str(phone1) == 'iPhone 14'

def tests_add(item1,phone1):
    assert phone1 + item1 == 15
    assert phone1 + phone1 == 10

