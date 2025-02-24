from functools import reduce

def multiply_all(numbers):
    return reduce(lambda x, y: x * y, numbers)

numbers = [1, 2, 3, 4, 5, 6]
result = multiply_all(numbers)
print(f"The result of multiplying: {result}")
