cars = ["audi", "mercedes benz", "bmw", "lambo", "lincoln", "ford"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

banned_users = ["cheekybugger113", "fan1010", "yomama191", "lighty11"]
user = "maria"

if user not in banned_users:
    print(f"{user.title()}, you are welcome to post in the chat! ")

# Amusement Park Example:
age = 12

if age < 4:
    price = "$0"
elif age < 18:
    price = "$25"
elif age < 65:
    price = "$40"
elif age >= 65:
    price = "$20"
print(f"Your price is {price}.")

# Pizzeria Example:
added_topping = ["anchovies", "mushrooms"]

if "pepperoni" in added_topping:
    print("Added Pepperoni")
if "mushrooms" in added_topping:
    print("Added Mushrooms")
if "anchovies" in added_topping:
    print("Added Anchovies")

print("Your Pizza is now ready!")

# Pizzeria Example Enhanced
available_toppings = ["green peppers", "mushrooms", "extra cheese", "olives", "pepperoni", "pineapple", "anchovies"]
requested_toppings = ["green peppers", "mushrooms", "french fries"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Added {requested_topping}!")
    else:
        print(f"Sorry, we don't have {requested_topping}!")
print("\nYour pizza is ready!")

