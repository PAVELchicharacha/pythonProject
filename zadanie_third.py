numbers = [1, 2, 3, 4, 5]
minimum, maximum = min(numbers), max(numbers)
index_minimum, index_maximum = (next((i for i, x in enumerate(numbers) if x == minimum)),
                                next((i for i, x in enumerate(numbers) if x == maximum)))
numbers[index_minimum], numbers[index_maximum] = maximum, minimum
print(numbers)
