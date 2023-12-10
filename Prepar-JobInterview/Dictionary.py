mydict = {
    'name': 'Hasibullah',
    'LastName': 'Aman',
    'age': 23
}

# for i in mydict:
#     print(mydict.keys())
#     print(mydict.values())

# print(mydict.items())
# mydict['name'] = 'Ali Ahmadi'
# print(mydict.items())

mydict.update({'university': 'Kabul University'})
# print(mydict)
for x, y in mydict.items():
    print(x, " : ", y)
