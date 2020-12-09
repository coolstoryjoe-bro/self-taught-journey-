usernames = ["jada", "richard", "julie", "horace", "vanessa", "admin"]

if usernames == []:
    print("We need more users!")
else:
    for username in usernames:
        if username == "admin":
            print(f"Hello {username}! Would you like to see a status report?")
        if username != "admin":
            print(f"Hello {username}! Thank you for logging in again!")

current_users = ["Hunky Dory33", "senpai554", "Badboy771", "jobo717", "Coolstoryj", "Floriien", "Help"]
new_users = ["Coolstoryj", "Jackson223", "halofanboy343", "Thisismyusername", "Floriien", "username3", "HELP"]
current_cap = current_users[:]

for user in new_users:
    if user in current_users and current_cap:
        print(f"This {user} is taken! Please create another one.")
    else:
        print(f"The username {user} is available.")

numbers = range(1, 10)

for number in numbers:
    if number < 2:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")