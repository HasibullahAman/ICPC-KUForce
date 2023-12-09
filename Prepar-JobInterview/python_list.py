# if our added item more than range, it will be added and other move accordingly.
# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)


# using insert method

name = ['Hasibullah','Elhama','Freshta','Zuhra','Hikmatullah']
name.insert(3,'Rohullah')
# print(*name)
name.append('Shikiba')
# print(*name)
# name.extend('Nawidullah')
# print(*name)


thislist = ["apple", "banana", "cherry"]
thistuple = {
    'name':'Hasibullah',
    'lastName':'Qasim'
}
thislist.extend(thistuple)
# print(thislist)


newNameList = name.remove("Elhama")
print(name)

# newNameList = name.pop(4)
# print(name)

# newNameList = name.pop()
# print(name)

del name[0]
print(name)

# we can completely delete a list using del
# del name
# print(name)
# name.clear()
# print(name)


