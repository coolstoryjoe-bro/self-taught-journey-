# # When you think an error may occur, you can write a try-except block to handle
# # the exception that might be raised.
#
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input(f"\nEnter first number: ")
    if first_number == 'q':
        break
    second_number = input(f"\nEnter second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

