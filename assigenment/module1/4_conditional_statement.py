# Practical Example 5: Write a Python program to find greater and less than a number using if_else. 
number1 = 49
number2 = 25

if number1 > number2:
    print("Number 1 is greater than of Number 2")
else:
    print("Number 1 is less than of Number 2")

# Practical Example 6: Write a Python program to check if a number is prime using if_else.

number = 85

if number <= 1:
    print("It's not a prime number")
else:
    if number % 2 == 0 or number % 3 == 0 or number % 6 == 0 or number % 7 == 0:
        print("It's not a prime number")
    else:
        print("It's prime number")

# Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder. 

percentage = 101

if percentage > 90 and percentage <= 100:
    print("A+ grade")
elif percentage > 80 and percentage <= 90:
    print("A grade")
elif percentage > 70 and percentage <= 80:
    print("Dictiontion grade")
elif percentage > 60 and percentage <= 70:
    print("B+ Grade")
elif percentage > 50 and percentage <= 60:
    print("B grade")
elif percentage > 40 and percentage <= 50:
    print("C grade")
elif percentage >= 35 and percentage <= 40:
    print("D grade")
elif percentage < 35 and percentage > 0:
    print("fail")
else:
    print("Invalid number")

# Practical Example 8: Write a Python program to check if a person is eligible to donate blood using a nested if. 

age = 18
blood_group = 'B'

if age >= 18:
    if blood_group == 'O-' or blood_group == 'O+' or blood_group == 'A+' or blood_group == "B+" or blood_group == 'AB+':
        print(f"You are eligible for blood donate")
    else:
        print("Invalid blood group")
else :
    print("You are not eligible for blood donate, because you are under age of 18")