l = [10, 20, 30, 40, 50]

k = iter(l)
print(next(k))
print(next(k))

print("Hello")

def test():
    yield "Hello"
    yield "python"

k = test()
print(next(k))
print(next(k))
print(next(k))