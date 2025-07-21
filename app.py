""" # create multiple restaurants w multiple or 1 item(s)
# keep track of stock
# compare profits

# restaturant manager for a chain of ur choice (sorta like janet's side quest) 
# 1) find average sales

class restaurant:
    def __init__(self, item, stock, price):
        self.item = item
        self.stock = stock
        self.price = price
        self.moneys = 0
    def sell(self):
        self.stock -= 1
        self.moneys += self.price
        print(f"{self.stock} items left. This restaurant currently has {self.moneys} dollars.")
    def inventory(self):
        print(f"This restaurant has {self.stock} {self.item} left.")

stockinput = input("How much stock does this restaurant have? ")
princeinput = input("How much does this item cost? ")
chipotle = restaurant("bowls", 10, 15)
chipotle.inventory() """


# managing chipotle orders
# customize bowl or burrito, can make multiple
# calculates total price + tax
import json
try:
    with open("orders.json", "r") as file:
        previous = input("you have orders saved in your cart. would you like to continue with them? ")
        if previous.lower() == "yes":
            orders = json.load(file)
        elif previous.lower() == "no":
            orders = []
except FileNotFoundError:
    orders = []
except json.JSONDecodeError:
    orders = []


class order:
    def __init__(self, item, base_price):
        self.item = item
        self.base_price = base_price
        self.price = 0
        self.toppings = []
    def add_toppings(self, topping):
        self.toppings.append(topping)
    def place_order(self):
        pre_tax = self.base_price + self.price
        total = pre_tax * 1.08875
        rounded = round(total, 2)
        dict = {
            "item" : self.item,
            "price" : rounded,
            "ingredients" : self.toppings
        }
        print(self.item)
        print(self.toppings)
        print(rounded)
        return dict

ask = input("would you like to place an order? ")

while ask == "yes":
    bb = input("would you like to build a bowl or a burrito? ")
    if bb.lower() == "burrito":
        chipotle = order("burrito", 10)
    elif bb.lower() == "bowl":
        chipotle = order("bowl", 10)

    protein = input("choose your protein: ")
    if protein.lower() == "honey chicken":
        chipotle.price += 2.40
        chipotle.add_toppings(protein)
    elif protein.lower() == "chicken" or protein.lower() == "sofritas" or protein.lower() == "veggie":
        chipotle.price += 1.80
        chipotle.add_toppings(protein)
    elif protein.lower() == "steak" or protein.lower() == "beef barbacoa":
        chipotle.price += 3.55
        chipotle.add_toppings(protein)
    elif protein.lower() == "carnitas":
        chipotle.price += 2.55
        chipotle.add_toppings(protein)
    else:
        print("we don't have this protein!")

    rice = input("would you like rice? ")
    if rice.lower() == "white rice":
        chipotle.add_toppings(rice)
    elif rice.lower() == "brown rice":
        chipotle.add_toppings(rice)

    beans = input("would you like any beans? ")
    if beans.lower() == "black beans":
        chipotle.add_toppings(beans)
    elif beans.lower() == "pinto beans":
        chipotle.add_toppings(beans)

    ask_top = input("would you like any toppings? ")
    while ask_top.lower() == "yes":
        each_top = input("which toppings would you like? ")
        if each_top.lower() == "adobo ranch":
            chipotle.price += 0.75
            chipotle.add_toppings(each_top)
        elif each_top.lower() == "guacamole":
            chipotle.price += 2.95
            chipotle.add_toppings(each_top)
        elif each_top.lower() == "queso":
            chipotle.price += 1.80
            chipotle.add_toppings(each_top)
        else:
            chipotle.add_toppings(each_top)
        ask_top = input("would you like any toppings? ")

    finish = input("are you ready to place your order? ")
    if finish.lower() == "yes":
        orders.append(chipotle.place_order())
    
    ask = input("would you like to place an order? ")
else: 
    with open("orders.json", "w") as file:
        json.dump(orders, file)

with open('orders.json', 'r') as file:
    orders_data = json.load(file)

total_order = 0

for order in orders_data:
    total_order += order['price']

print(f"your total is ${total_order}")
