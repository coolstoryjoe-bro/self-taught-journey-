# Example 1:

# alien_0 = {'color': 'yellow', 'points': 5}
# alien_1 = {'color': 'green', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
  #  print(alien)

# Example 2

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow',}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[:5]:
    print(alien)
print('...')

print(f'Total number of aliens: {len(aliens)}.')


pizza = {
    'crust': 'thick',
    'toppings': ['extra cheese', 'mushrooms'],
    }

print(f"The pizza you ordered is: {pizza['crust']}- \nThe toppings "
      f"you ordered are:")
for topping in pizza['toppings']:
    print(f'\t{topping}')

