l = [1, 2, 3, 4, 5, 6, 7, 8]
# n = []
# def square(a):
#     return a*a

# for i in l:
#     k = square(i)
#     n.append(k)

# print(n)

# sq = map(square, l)
# print(list(sq))

# n = map(lambda k: k * k, l)
# print(list(n))

subjects = ["java", "python", "android", "node", "react"]

length = map(lambda a: len(a), subjects)
print(list(length))

num1 = [10, 20, 30, 40, 50]
num2 = [1, 2, 3, 4, 5]

table = map(lambda a, b: a * b, num1, num2)
print(list(table))

