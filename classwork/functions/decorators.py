# def before(func):
#     def execute():
#         print("calling before test")
#         func()
#     return execute

# def after(func):
#     def execute():
#         func()
#         print("calling after test")
#     return execute

# @after
# @before
# def test():
#     print("Calling the test function")

# test()

# def add(func):
#     def execute(*a):
#         sum = 0
#         for i in a:
#             sum += i
#         print(f"addition is {sum}")
#         func(*a)
#     return execute

# @add
# def calc(a, b):
#     pass

# calc(10, 20)

def numbers_only(func):
    def execute(a):
        if str(a).isdigit():
            func(a)
        else:
            print("Invalid Input")
    return execute

def chars_only(func):
    def execute(a):
        if str(a).isalpha():
            func(a)
        else:
            print("Invalid Input")
    return execute

# @numbers_only
@chars_only
def get(a):
    print(a)

get("ddasd")