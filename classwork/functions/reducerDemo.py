from functools import reduce

l = [5, 4, 6, 9, 8, 7, 3 ,2 , 0, 1]

k = reduce(lambda a, b: a + b, l)
max = reduce(lambda a, b: a if a > b else b, l)
min = reduce(lambda a, b: a if a < b else b, l)
print(min)
