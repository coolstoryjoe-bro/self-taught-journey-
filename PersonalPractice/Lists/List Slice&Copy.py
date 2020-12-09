players = ["claire", "claudia", "clover", "lucy", "alicia", "hazel"]
print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())

my_foods = ["falafel", "hamburger", "fries", "nachos", "churros"]
friends_foods = my_foods[:]

print("My favorite foods are: ", my_foods)

print("\nMy friend's favorite foods are: ", friends_foods)

print("\nWe decided to add dessert to our foods list!")

my_foods.append("vanilla icecream")
friends_foods.append("cake")

print("\nMy favorite foods are: ", my_foods)

print("\nMy friend's favorite foods are: ", friends_foods)
