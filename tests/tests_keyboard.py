import pytest
from src.keyboard import Keyboard

@pytest.fixture
def keyboard():
    return Keyboard('Товар 3', 5, 10)

def test_keyboard(keyboard):
    assert str(keyboard) == 'Товар 3'
    assert repr(keyboard) == "Keyboard('Товар 3', 5, 10)"

    assert keyboard.language == 'EN'
    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang()
    assert keyboard.language == 'EN'
