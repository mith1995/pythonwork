numbers = [11, 21, 17, 8, 23, 30, 12]

# Write a Python program to apply the map() function to square a list of numbers. 

squares = map(lambda x: x * x, numbers)
print(list(squares))

# Write a Python program that uses reduce() to find the product of a list of numbers. 
from functools import reduce

total_sum = reduce(lambda x, y: x + y, numbers)
print(total_sum)

# Write a Python program that filters out even numbers using the filter() function. 

even_numbers = filter(lambda a: a % 2 == 0, numbers )
print(list(even_numbers))