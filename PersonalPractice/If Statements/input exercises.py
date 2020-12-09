admin_message = "Let me know how you are doing!"
admin_message += "\nHow are you doing? "

hayd = input(admin_message)
print(f"You are doing {hayd}")

car_message = input("Enter the car you're looking for: ")

print(f"Let's see if we can find a {car_message} for you.")

seating = input("How many people are you seating? ")
seatings = int(seating)

if seatings > 8:
    print("Sorry! You'll have to wait for a table.")
else:
    print("Come on in m8. We got you a table.")

    num_0 = input("Enter a number: ")
    numeral = int(num_0)

    if numeral % 10 == 0:
        print("It is a multiple of 10")
    else:
        print("Nope.")
