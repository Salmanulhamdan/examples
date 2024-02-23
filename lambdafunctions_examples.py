#  A simple lambda function
square = lambda x: x ** 2
print(square(5))


# Lambda function with multiple arguments

multiply = lambda x, y: x * y
print(multiply(3, 7))


# Using a lambda function inside another function

def my_func(n):
    return lambda x: x * n

doubler = my_func(2)
print(doubler(5))



# Using lambda with Python built-in functions

my_list = [1, 2, 3, 4, 5, 6]
odd_numbers = list(filter(lambda x: x % 2 != 0, my_list))
print(odd_numbers)


# Using lambda function for sorting

my_list = [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)


# Using a lambda function to return a function

def my_func(n):
    return lambda x: x + n

adder = my_func(5)
print(adder(10))



# Using a lambda function in list comprehension

my_list = [1, 2, 3, 4, 5, 6]
new_list = [(lambda x: x ** 2)(x) for x in my_list]
print(new_list)


# Using a lambda function to sort a list of strings by the last character

my_list = ["apple", "banana", "cherry"]
sorted_list = sorted(my_list, key=lambda x: x[-1])
print(sorted_list)


# Using a lambda function with the reduce function

from functools import reduce

my_list = [1, 2, 3, 4, 5]
product = reduce((lambda x, y: x * y), my_list)
print(product)




# Using a lambda function with the map function

my_list = [1, 2, 3, 4, 5]
new_list = list(map(lambda x: x ** 2, my_list))
print(new_list)