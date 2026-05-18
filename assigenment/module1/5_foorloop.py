# Practical Example 1: Write a Python program to print each fruit in a list using a simple for loop. List1 = ['apple', 'banana', 'mango']

List1 = ['apple', 'banana', 'mango']
for fruit in List1:
    print(fruit)

# Practical Example 2: Write a Python program to find the length of each string in List1. 

List1 = ['apple', 'banana', 'mango']
for fruit in List1:
    print(len(fruit))

# Practical Example 3: Write a Python program to find a specific string in the list using a simple for loop and if condition. 

List1 = ['apple', 'banana', 'mango']
for fruit in List1:
    if fruit == 'apple':
        pass
    else:
        print(fruit)

# Practical Example 4: Print this pattern using nested for loop: 
# markdown 
# Copy code 
# * 
# ** 
# *** 
# **** 
# ***** 

for j in range(0, 5):
    for i in range(j + 1):
        print("*", end="")
    print("")