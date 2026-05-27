l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# r = []
# def checkodd(n):
#     if n % 2 != 0:
#         return n
    
# for i in l:
#     k = checkodd(i)
#     if k is not None:
#         r.append(k)
# print(r)

# r = filter(checkodd, l)
# r = filter(lambda a: a % 2 != 0, l)
# print(list(r))

subjects = ["java", "python", "android", "node", "react", "php"]

a_contain = filter(lambda word: "a" in word, subjects)
print(list(a_contain))

start_with_p = filter(lambda word: word.startswith("p"), subjects)
print(list(start_with_p))

result_square = filter(lambda n: n != 1 and (n ** 0.5) % 1 == 0, l)
print(list(result_square))