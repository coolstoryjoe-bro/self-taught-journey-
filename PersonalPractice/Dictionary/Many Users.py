users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f'\nUsername: {username}')
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")


users = {
    'smaqbool': {
        'first': 'saiyad',
        'last': 'maqbool',
        'location': 'elk grove',
    },
    'arussell': {
        'first': 'audrey',
        'last': 'russell',
        'location': 'elk grove',
    },
}

for names, user_information in users.items():
    print(f"\nUsername: {names}")
    full_name = f"{user_information['first']} {user_information['last']}"
    location = f"{user_information['location']}"

    print(f"\tFull Name: {full_name.title()}")
    print(f"\tUser Location: {location.title()}")

