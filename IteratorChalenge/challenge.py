numbers = [1, 2, 3, 4, 5, 6, 7 ,8 ,9]

number_iterator = iter(numbers)

for i in range(0, len(numbers)):
    print(next(number_iterator))
