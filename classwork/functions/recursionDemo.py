# def test(a):
#     print(a*a)
#     a += 1
#     if a < 20:
#         test(a)

# test(1)

# Factorial: 5 * 4 * 3 * 2 * 1 = 120

def fact(num):
    sum = 0
    if num >= 1:
        sum += num * (num - 1)
        num -= 1
    return sum
print(fact(5))

