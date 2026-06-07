# txt = "I love apples,\tapple are my favorite fruit"
# format_txt = "For only {price:.2f} dollars!"


# print(txt.capitalize()) # First character convert into upper case
# print(txt.casefold()) # converts strings into lower case
# print(txt.center(100)) # Return centerd string with the space
# print(txt.count("apple")) # Returns the number of times a specified value occurs in a string
# print(txt.encode())
# print(txt.endswith("fruit!")) # Returns true if the string ends with the specified value
# print(txt.expandtabs(10))
# print(txt.find('are'))
# print(format_txt.format(price=50))
# print(txt.index("are"))
# print("txt23".isalnum()) # This characters are not alphanumeric: space!@#$%^&*()
# print("helloworld".isalpha())
# print("12345".isdecimal()) # Returns True if all characters in the strings are decimals: (0-9)
# print("12345".isdigit())
# print("hello world".islower())
# print("12356".isnumeric())
# print("  ".isspace())
# print("Hello Wordl".istitle())
# print("HELLO WORLD".isupper())
# print(txt.partition('are'))
# print(txt.replace('apple', 'mangeo', 1))
# print(txt.rfind('apple'))


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# print(thislist[2:5])
# print(thislist[:4])
# print(thislist[2:])
# print(thislist[-4:-1])

# thislist[1] = "blackcurrant"
# thislist[1:3] = ["blackcurrant", "watermelon"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# thislist[1:3] = ["watermelon"]
# thislist.insert(2, "watermelon")
thislist.append("orange")

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)

# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)

# thislist.remove("orange")
# thislist.pop(3)
# del thislist[1]
# del thislist
# thislist.clear()

# thislist.sort(reverse=True)
# thislist.reverse()

# mylist = thislist.copy()
# mylist = list(thislist)
# mylist = thislist[:]
# mylist[0] = "Angoor"
# print(mylist)
# print(thislist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
