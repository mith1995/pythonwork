# Write a Python program to demonstrate string slicing. 
""" text = "Python Programming"

print("Original String:", text)
print("first 6 characters:", text[:6])
print("character from index 7 to 17:", text[7:17])
print("From index 7 to end:", text[7:])
print("Every second character:", text[::2])
print("Reverse string:",text[::-1]) """

# Write a Python program that manipulates and prints strings using various string methods.

text = "Python Programming"
# text = "नमस्ते"
# text = "H\te\tl\tl\to"

print("Convert first character to upper case:", text.capitalize())
print("convert string into lower case:", text.casefold())
print("Returns center string with number of space:", len(text.center(20)))
print("Returns number of times occurs:", text.count('Python'))
print("Returns encoded string:", text.encode(encoding='utf-8'))
print("Return True if the string end with specified value:", text.endswith('programming'))
print("Set the tab size in string:", text.expandtabs(10))
print("Return the position of where it was found:", text.find("Pro"))
print("Return the position otherwise not found string it generate error:", text.index("Pro"))
print("Return True if all characters are alphanumeric:", text.isalnum())
print("Return True if all characters are alpha:", "pythonProgramming".isalpha())
print("convert string into lower case:", text.lower())

myTuple = ("John", "Peter", "Vicky")
print("Join Tuple into the string:", "#".join(myTuple))