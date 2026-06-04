print("Program Start")

try:
    a = 10
    b = a/0
except Exception as e:
    print(e)
else:
    print("Code run successfully")
finally:
    print("always executable block")

print("Program ended")