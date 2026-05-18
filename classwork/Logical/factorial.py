# number = 5
# fact = 1
# for i in range(number, 0, -1):
#     fact = fact * i

# print(fact)

# 1 * 2 = 2
# 2 * 2 = 4
price = 1
total = 0
for i in range(1, 31):
    price = price * 2
    total += price
    print(f"{i} : {price}")

print(total)