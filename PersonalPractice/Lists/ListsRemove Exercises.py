dinner_guests = ["Jose Abad", "Layden Abad", "DenMarie Abad", "Audrey Russell", "Sarah Abad"]
print("Those who are invited: ", dinner_guests)

print("Sarah Abad can't make it to dinner. :( ")

cannot_come = dinner_guests.pop(4)
dinner_guests.append("Colby Cuthbertson")
print("New list of invites: ", dinner_guests)

print("It seems I have found a larger table!")

dinner_guests.insert(0, "Saiyad Maqbool")
dinner_guests.insert(1, "Tami")
print("These are the new invites: ", dinner_guests)

print("Sorry I could only find a table for two people!")

uninvited_1 = dinner_guests.pop(0)
print("Sorry Saiyad, I could only find a table for two people!")
uninvited_2 = dinner_guests.pop(0)
print("Sorry Tami, I could only find a table for two people!")
uninvited_3 = dinner_guests.pop(2)
print("Sorry Audrey, I could only find a table for two people!")
uninvited_4 = dinner_guests.pop(2)
print("Sorry Colby, I could only find a table for two people!")
uninvited_5 = dinner_guests.pop(2)

print(dinner_guests)

message_3 = f"Hey {dinner_guests[0]}! You're invited to dinner!"
message_4 = f"Hey {dinner_guests[1]}! You're invited to dinner!"

print(f"Hello {dinner_guests[0]}, you are formally invited to dinner.")
print(f"Hello {dinner_guests[1]}, you are formally invited to dinner.")

del dinner_guests[0]
del dinner_guests[0]

print(dinner_guests)
