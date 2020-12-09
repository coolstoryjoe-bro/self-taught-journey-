
for value in range (1, 6):
    print(value)

numbers = list(range(1, 10))
print(numbers)

numbers_1 = list(range(2, 11, 2))
print(numbers_1)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

squares_1 = [value**2 for value in range(1, 11)]
print(squares_1)

for value in range(1, 21, 3):
    print(value)

cubes_1 = []
for value in range(1, 10):
    cube = value ** 3
    cubes_1.append(cube)
print(cubes_1)

cubes = [value**3 for value in range(1, 10)]
print(cubes)

