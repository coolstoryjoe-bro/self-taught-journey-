toppings_quest = "\nWhat pizza toppings would you like? "
toppings_quest += "\n(Enter 'done' to send the toppings.) "
message = ""

active = True
while active:
    message = input(toppings_quest)

    if message == 'done':
        active = False
    else:
        print(f"Adding {message.title()} to you pizza.")



movie_quest = "\nWhat is your age? "
movie_quest += "\n(Type and enter 'done' when finished.) "

active = True
while active:
    input_0 = input(movie_quest)
    message = int(input_0)

    if message == 'done':
        active = False
    elif message >= 12: # I couldn't figure this out so I used the long way.
        print("Your movie ticket cost is: $15")
    elif message < 12:
        if message == 11: # I couldn't figure out the range so I did it the long way.
            print("Your ticket cost is: $10")
        if message == 10:
            print("Your ticket cost is: $10")
        if message == 9:
            print("Your ticket cost is: $10")
        if message == 8:
            print("Your ticket cost is: $10")
        if message == 7:
            print("Your ticket cost is: $10")
        if message == 6:
            print("Your ticket cost is: $10")
        if message == 5:
            print("Your ticket cost is: $10")
        if message == 4:
            print("Your ticket cost is: $10")
        if message <= 3:
            print("Your ticket cost is: Free")

# I SPENT SO LONG IN THIS NEXT PIECE OF CODE. Exercise 7-6 pg 124.
movie_quest = "\nWhat is your age? "
movie_quest += "\n(Type and enter 'done' when finished.) "
message = ""

active = True
while active:
    message = input(movie_quest)

    if message == 'done':
        break
    if message != 'done':
        message_1 = int(message)
        equation = message_1 > 3
        if message_1 >= 12:
            print("Cost of ticket: $15")
        elif message_1 < 12 and equation:
            print("Cost of ticket: $10")
        else:
            print("Cost of ticket: Free")

# Infinite Loop example
x = 2
while x <= 20:
    x += 1
    print(x)
