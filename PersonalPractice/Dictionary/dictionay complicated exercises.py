
people = [{
    'username': 'floriien',
    'first': 'audrey',
    'last': 'russell',
    'favorite number': [3, 6, 8],
    }, {
    'username': 'maqnchz',
    'first': 'saiyad',
    'last': 'maqbool',
    'favorite number': [9],
    }, {
    'username': 'hellocolby',
    'first': 'colby',
    'last': 'cuthbertson',
    'favorite number': [7, 6],
    }, ]

for users in people:
    print(f"\nUsername: {users['username']}")
    full_name = f"{users['first']} {users['last']}"
    print(f"\tFull Name: {full_name.title()}")
    print(f"\tFavorite Number(s): {users['favorite number']}")

pets = [{
    'pet type': 'dog',
    'owner first': 'claudia',
    'owner last': 'rutherford',
    }, {
    'pet type': 'cat',
    'owner first': 'jason',
    'owner last': 'huller',
    }, {
    'pet type': 'bird',
    'owner first': 'bridgette',
    'owner last': 'leatherwoman',
    },]

for pet in pets:
    print(f"\n\tPet type: {pet['pet type']}")
    owner_full = f"{pet['owner first']} {pet['owner last']}"
    print(f"\tOwner Full Name: {owner_full.title()}")

favorite_places = [{
    'favorite place': 'cabo',
    'friend first': 'julie',
    'friend last': 'holmes',
}, {
    'favorite place': 'maldives',
    'friend first': 'betty',
    'friend last': 'smith',
}, {
    'favorite place': 'dubai',
    'friend first': 'gober',
    'friend last': 'townes',
}]

for friends in favorite_places:
    friends_full = f"{friends['friend first']} {friends['friend last']}"
    print(f"\n\tMy friend's full name: {friends_full.title()}")
    print(f"\tMy friends favorite place: {friends['favorite place']}")

cities = {
    'sacramento': {
        'country': 'united states',
        'population': 150_000,
        'fun fact': 'i live in the county',
    },
    'london': {
        'country': 'britain',
        'population': 450_000,
        'fun fact': 'used to be called londoninium',
    },
    'paris': {
        'country': 'france',
        'population': 335_000,
        'fun fact': 'has the eiffel tower',
    },
}

for city, city_info in cities.items():
    print(f"\nThis is the city: {city.title()}")
    compiled_info = f"\n\tThis is the city information: " \
                    f"\n\t\tHome Country: {city_info['country']}" \
                    f"\n\t\tCity's population: {city_info['population']}" \
                    f"\n\t\tCity's fun fact: {city_info['fun fact']}"
    print(compiled_info.title())