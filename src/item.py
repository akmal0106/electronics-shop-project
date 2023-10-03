class Item():
    pay_rate = 1.0
    all = []

    def __init__(self, product_name, product_cost, product_quantity):
        Item.all.append(self)
        self.product_name = product_name
        self.product_cost = product_cost
        self.product_quantity = product_quantity

    def calculate_total_price(self):
        return self.product_cost * self.product_quantity

    def apply_discount(self):
        return self.product_cost * self.product_quantity * self.pay_rate

    def price(self):
        # result = (self.product_cost * self.product_quantity) - (self.product_cost * self.product_quantity * self.pay_rate)
        return round((self.product_cost * self.product_quantity) - (self.product_cost * self.product_quantity * self.pay_rate))