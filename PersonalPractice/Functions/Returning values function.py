# Returning a value using 3 parameters or two.

def get_formatted_name(first_name, last_name, middle_name="",):
    """Return a fullname, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'hooker')
print(musician)

# Returning a Dictionary

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# Using a function with a while loop:

def get_formatted_name(first_name, last_name):
    """Return formatted full name."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

    # This is an infinite loop! Without the breaks & if statements
while True:
    print("\nPlease tell me your name:")
    print("\nEnter 'q' anytime to quit!")
    f_name = input("First Name: ")
    if f_name == 'q':
        break
    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


# DIY 1
def city_country(city, country):
    city_and_country = f"{city}, {country}"
    return city_and_country.title()

city_combo_1 = city_country('paris', 'france')
city_combo_2 = city_country('london', 'england')
city_combo_3 = city_country('new york', 'united states')

print(city_combo_1)
print(city_combo_2)
print(city_combo_3)

# DIY 2
def make_album(name, album, songs=None):
        album_1 = {'name': name, 'album': album, 'songs': songs}
        if songs:
            album_1['songs'] = songs
        return album_1

musician = make_album('yaosobi', 'running into night')
print(musician)


# DIY 3
def make_album(artist, title):
    album = {'artist': artist, 'title': title, }
    return album

while True:
    print(f"\nPlease tell me the name of artist and album: ")
    print(f"Type 'quit' if you're done answering. ")
    artinp = input("\nWho is the artist? ")
    if artinp == 'quit':
        break
    artinp_1 = input("What is the title? ")
    if artinp_1 == 'quit':
        break

    inputted_albums = make_album(artinp, artinp_1)
    print(f"\n{inputted_albums}")

