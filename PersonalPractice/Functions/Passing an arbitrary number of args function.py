# Edit 1

def make_pizza(*toppings): # The * makes a tuple. Often you'll see default value *args in other programs.
    """print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers', 'extra cheese')

# Edit 2

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers', 'extra cheese')

# Mixing several positional and arbitrary arguments:
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size}- inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Using arbitrary keyword arguments:
def build_profile(first, last, **user_info): # The ** makes a dictionary.
    # Often you'll see default value **kwargs in other programs.
    """Build a dictionary containing everything we know about a user."""
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

# DIY 1
def requested_ingredients(*ingredients):
    """This prints out the following ingredients."""
    print(f"Your sandwich is being made with the following ingredients: ")
    print(ingredients)

requested_ingredients('meatballs', 'lettuce')
requested_ingredients('meatballs', 'lettuce', 'tomatoes', 'salami', 'jesus')
requested_ingredients('meatballs', 'lettuce', 'tomatoes', 'salami', 'jesus', 'bread')