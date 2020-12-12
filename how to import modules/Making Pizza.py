# This .py file is the program that the function of pizza.py is being import too.

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Using 'as' to Give a FUNCTION an alias.
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

    # General syntax for this is:
    from module_name import function_name as fn

# Using 'as' to Give a MODULE an alias/
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing All Fucntions in a Module:
from pizza import *
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# from module_name import *
