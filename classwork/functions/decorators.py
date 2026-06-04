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

def add(func):
    def execute(*a):
        sum = 0
        for i in a:
            sum += i
        print(f"addition is {sum}")
        func(*a)
    return execute

@add
def calc(a, b):
    pass

calc(10, 20)