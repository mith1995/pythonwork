def test():
    print("Test calling")

def square(a):
    print(a * a)

def add(a, b):
    print(a + b)

def message():
    return "Hello"

def cube(a):
    return a * a * a

test()
square(10)
add(10, 20)
print(message())
print(cube(12))

# def person(name, email, age):
#     print(name, email, age)

# person("abc", "abc@gmail.com", 25)

# def person(name, email="xyz@gmail.com", age=30):
#     print(name, email, age)

# person("abc", age=25)

# def marks(math, science=73, english=35):
#     print(math, science, english)

# marks(70, english=63)

# def sum(*a):
#     sum = 0
#     for i in a:
#         sum += i
#     print(sum)

# sum(10, 20, 30, 40, 50)

# def student(**a):
#     print(a)

# student(name="mithlesh", email="mithlesh@gmail.com", age=29)

add = lambda a, b: a + b
sq = lambda a: a*a

print(add(10, 20))
print(sq(10))