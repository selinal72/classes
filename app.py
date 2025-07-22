# managing chipotle orders
# customize bowl or burrito, can make multiple
# saves orders to json file so u can continue 
# calculates total price + tax
import json
try:
    with open("orders.json", "r") as file:
        previous = input("you have orders saved in your cart. would you like to continue with them? ").lower()
        if previous == "yes":
            orders = json.load(file)
        elif previous == "no":
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

with open('menu.json', 'r') as file:
    menu_data = json.load(file)

protein_menu = []
topping_menu = []

for addon in menu_data:
    if addon["type"] == "protein":
        protein_menu.append(addon)
    else:
        topping_menu.append(addon)

ask = input("would you like to place another order? ").lower()

while ask == "yes":
    bb = input("would you like to build a bowl or a burrito? ").lower()
    if bb == "burrito":
        chipotle = order("burrito", 10)
    elif bb == "bowl":
        chipotle = order("bowl", 10)

    protein = input("choose your protein: ").lower()
    for meat in protein_menu:
        if protein == meat["name"]:
            chipotle.price += meat["price"]
            chipotle.add_toppings(protein)

    rice = input("choose your rice: ").lower()
    if rice == "white rice" or rice == "brown rice":
        chipotle.add_toppings(rice)

    beans = input("choose your beans: ").lower()
    if beans == "black beans" or beans == "pinto beans":
        chipotle.add_toppings(beans)

    ask_top = input("would you like any toppings? ").lower()
    while ask_top == "yes":
        each_top = input("which toppings would you like? ").lower()

        for top in topping_menu:
            if each_top == top["name"]:
                chipotle.price += top["price"]
        chipotle.add_toppings(each_top)

        ask_top = input("would you like any toppings? ").lower()

    finish = input("are you ready to place your order? ").lower()
    if finish == "yes":
        orders.append(chipotle.place_order())
    
    ask = input("would you like to place another order? ").lower()
else: 
    with open("orders.json", "w") as file:
        json.dump(orders, file)

with open('orders.json', 'r') as file:
    orders_data = json.load(file)

total_order = 0

for order in orders_data:
    total_order += round(order['price'], 2)

print(f"your total is ${total_order}")
