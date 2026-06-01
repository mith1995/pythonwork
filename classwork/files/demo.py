# f = open('./classwork/files/test.txt', 'w')
# f.write("Hello World")
# f.writelines(["python\n", "Java\n", "Node"])
# f.close()

# f = open('./classwork/files/test.txt', 'r')
# data = f.read()
# print(data)

# f = open('./classwork/files/test.txt', 'a')
# f.write("I Love India")
# f.close()
# print("File Path")

# f = open("./classwork/files/test.txt", "r")
# data = f.readlines()
# data = f.readline()
# print(data)

# while True:
#     data = f.readline()
#     if data.startswith('p'):
#         print(data)
#     if not data:
#         break

# with open("./classwork/files/test.txt", 'r') as f:
#     print(f.seek(10)) #Change the cursor position while read the file
#     print(f.tell()) #Get the cursor position
#     data = f.read()
#     print(f.tell())
#     print(data)

"""
1. r+ => first check file exists or not otherwise generate error and after than write the content, 
2. w+ => If file not exists it create and write the content and afterthan read the file 
3. a+ => Append function create, write, read, and update the file
"""
# with open("./classwork/files/home.txt", 'a+') as f: 
#     f.write("write programming")
#     f.seek(0)
#     data = f.read()
#     print(data)

# with open("./classwork/files/a.jpeg", 'rb') as f:
#     data = f.read()
#     print(data)

# import json
# k = {"name": "abc", "email": "abc@gmail.com"}

# with open("./classwork/files/data.json", "w") as f:
#     json.dump(k, f)

# with open("./classwork/files/data.json", 'r') as f:
#     data = json.load(f)
#     print(data)

file_name = input("Enter a file name: ")

with open(f"./classwork/files/{file_name}", 'a+') as f:
    f_content = input(f"Insert the content in {file_name}: ")
    f.write(f"\n{f_content}")
    f.seek(0)
    data = f.read()
    print(data)