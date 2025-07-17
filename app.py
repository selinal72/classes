# create multiple restaurants w multiple or 1 item(s)
# keep track of stock
# compare profits

class restaurant:
    def __init__(self, item, stock, price):
        self.item = item
        self.stock = stock
        self.price = price
        self.moneys = 0
    def sell(self):
        self.stock -= 1
        self.moneys += self.price
        print(f"{self.stock} items left. {self} currently has {self.moneys} dollars.")

chipotle = restaurant("bowls", 10, 15)
chipotle.sell()

