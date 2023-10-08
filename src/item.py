import csv

class Item():
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__()
        self.__name= name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls, filename):
        with open(filename, encoding='windows-1251') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row['name']
                price = row['price']
                quantity = row['quantity']
                item = cls(name, price, quantity)
                cls.all.append(item)

    @staticmethod
    def string_to_number(string):
        try:
            return int(float(string))
        except ValueError:
            number = None
        return number



