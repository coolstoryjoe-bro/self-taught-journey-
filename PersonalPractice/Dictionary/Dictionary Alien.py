alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x-coordinate'] = 0
alien_0['y-coordinate'] = 25
new_points = alien_0['points']
print(f"You earned {new_points} points!")
print(alien_0)

# Modifying Values in Dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}")

alien_0 = {'color': 'yellow'}
print(f"The alien is now {alien_0['color']}")

# This is a more complicated Dictionary code
alien_0 = {'x-coordinate': 0, 'y-coordinate': 25, 'speed': 'medium'}
print(f"Original Position: {alien_0['x-coordinate']}")

# Move alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    alien_0['speed'] == 'fast'
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x-coordinate'] = alien_0['x-coordinate'] + x_increment

print(f"New position: {alien_0['x-coordinate']}")

# Dictionaries Try Yourself:
master_boogway = {'mbugua': 'munyutu', 22: 'stockton'}
print(master_boogway)

favorite_numbers = {'mbugua': 7, 'audrey': 6, 'saiyad': 5, 'ashley': 4}

glossary = {
    'tuple': 'You use ()',
    'list': 'You use []',
    'dictionary': 'You use {}',
    'bool': 'Conditional T/F',
    'int': 'integers',
    }

for word, definitions in glossary.items():
    print(f'This is the word: {word.title()}. \n\tThis is the definition: '
          f'{definitions.title()}.')

# Friends/languages:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(f'\n\t{name.title()}, thank you for taking the poll!')

print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(f'\t{language.title()}')

friends = ['sarah', 'phil']
for names in favorite_languages.keys():
    print(f'Hi {names.title()}')

    if names in friends:
        language = favorite_languages[names].title()
        print(f'\t{names.title()}, I see you love {language.title()}')

major_rivers = {'nile': 'egypt', 'euphrates': 'afghanistan', 'rhine': 'germany'}

for rivers, country in major_rivers.items():
    print(f'{rivers.title()} river runs through {country.title()}.')

for rivers in major_rivers.keys():
    print(rivers)

for country in major_rivers.values():
    print(country)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are: ")
    for language in languages:
        print(f"\t{language.title()}")


