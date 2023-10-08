from src.item import Item

class Mixinchange:
    en_lang = 'EN'
    ru_lang = 'RU'

    def __init__(self):
        self.language = self.en_lang

    def change_lang(self):
        if self.language == self.en_lang:
            self.language = self.ru_lang
            return self.language
        else:
            self.language = self.en_lang
            return self.language

class Keyboard(Item, Mixinchange):
    pass
