def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# Passing information to a function:

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}")

greet_user('jesse')

# Function DIY:
def message():
    """printing one message"""
    print("I am learning about functions. :)")
message()

def favorite_book(title):
    """prints the title of my favorite book"""
    print(f"One of my favorite books is {title.title()}")

favorite_book("Alice in Wonderland")

def describe_pet(animal_type, pet_name):
    """Display animal type and name of pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('dog', 'artemis')
describe_pet('hamster', 'willie')


# Default Values

def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")

describe_pet(pet_name='Willie')


# Functions DIY:
def make_tshirt(text, size='large'):
    print(f"The size of the t-shirt: {size}, and the text on the t-shirt: {text}")

make_tshirt('I love python!')

def describe_city(name, country='france'):
    print(f"{name} is in {country}")

describe_city(name='paris')
describe_city('budapest')
describe_city(name='paris', country='new york')