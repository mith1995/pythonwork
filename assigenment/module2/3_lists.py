fruits = ["apple", "orange", "mangeo"]

# Write a Python program to iterate over a list using a for loop.
for fruit in fruits:
    print(fruit)

# Write a Python program to sort a list using both sort() and sorted(). 
# sort()
fruits.sort(reverse=True)


# sorted()
new_sorted = sorted(fruits)
# print(new_sorted)
# print(fruits)

# 5) Write a Python program to iterate through a list and print each element. 
for fruit in fruits:
    print(fruit)

flowers = []
# 6) Write a Python program to insert elements into an empty list using a for loop and append(). 

for i in range(len(fruits)):
    flowers.append(fruits[i])

print(flowers)