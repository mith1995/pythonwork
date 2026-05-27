student = {
    "name": "mithilesh",
    "email": "mithilesh@gmail.com",
    "age": 20
}

# print(student['name'])
# print(student.get('name'))

# print(student.keys())
# print(student.values())
# print(student.items())

#Update or add item in the dictionary while key not exists item added in the dictionary otherwise update item 
# student['name'] = 'xyz'
# student.update({'name': 'xyz'})
# print(student)

# student.pop('name')
# student.popitem()
# del student
# del student['name']
# student.clear()
# print(student)

for i in student:
    print(i)