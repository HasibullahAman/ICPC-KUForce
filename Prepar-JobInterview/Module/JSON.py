import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

parsList = json.loads(x)

# print(parsList['name'])

mydict = {
    'name' : 'Hasibullah',
    'LastName' : "Aman",
    'age' : 23
}

changeToJson = json.dumps(mydict)


print(changeToJson)