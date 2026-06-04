# Write a generator function that generates the first 10 even numbers.

def even_numbers():
    for i in range(2, 21, 2):
        yield i

for num in even_numbers(): 
    print(num)

# Write a Python program that uses a custom iterator to iterate over a list of integers. 

my_list = [10, 20, 30]
iterator = iter(my_list)

print(next(iterator))
print(next(iterator))
print(next(iterator))