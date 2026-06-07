fruits = ["apple", "orange", "mangeo"]

# Write a Python program to add elements to a list using insert() and append(). 
# Insert()
fruits.insert(1, "Watermelon")

# Append()
fruits.append("Black berry")

# Write a Python program to remove elements from a list using pop() and remove(). 
#  Remove()
fruits.remove("orange")

# Pop()
del_fruit = fruits.pop(-2)
print(fruits)
print(del_fruit)