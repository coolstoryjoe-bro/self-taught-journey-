sandwich_orders = ["BLT", "new jersey style", "boston style", "pastrami", "steak",
                   "subway", "pastrami", "chicago style", "pastrami"]
finished_sandwiches = []

print("Deli has run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    progress_sandwich = sandwich_orders.pop()
    print(f"Your {progress_sandwich.title()} is being made!")
    finished_sandwiches.append(progress_sandwich)
    continue

for sandwiches in finished_sandwiches:
    print(f"\tI made you a {sandwiches} sandwich!")

# Last DIY in Dictionary Chapter 7

    responses = {}

    polling_active = True

    while polling_active:
        user = input(f"Enter your name: ")
        vacation = input(f"What is your dream vacation? ")
        responses[user] = vacation

        repeat = input(f"Do you want to ask someone else to take this poll? yes/no ")
        if repeat == 'no':
            polling_active = False

    print("\n___Polling Results___")
    for user, vacation in responses.items():
        print(f"{user} \nDream Vacation: {vacation}")