import json

numbers = [1, 2, 3, 4, 5, 6]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

with open(filename) as f:
    numbers = json.load(f)

print(numbers)