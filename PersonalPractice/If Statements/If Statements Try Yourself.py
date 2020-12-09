alien_colors = ["green", "orange", "blue", "purple", "yellow"]

if "green" in alien_colors:
    print("You have earned 5 points!")
elif "orange" in alien_colors:
    print("You have earned 10 points!")
elif "blue" in alien_colors:
    print("You have earned 15 points!")
elif "purple" in alien_colors:
    print("You have earned 20  points!")
elif "yellow" in alien_colors:
    print("You have earned 25 points!")
else:
    print("You have earned 0 points!")

user_input = input("Enter your age: ")
age = int(user_input)

if age < 2:
    print("You are a baby!")
if age < 4:
    print("You are a toddler!")
if age < 13:
    print("You are a kid!")
if age < 20:
    print("You are a teenager!")
if age < 65:
    print("You are an adult!")
if age >= 65:
    print("You are a senior!")


