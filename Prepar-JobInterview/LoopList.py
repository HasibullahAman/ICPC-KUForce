# Looping Using List Comprehension
name = ['Hasibullah', 'Elhama', 'Freshta', 'Zuhra', 'Hikmatullah']
# [print(i) for i in name]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
'''
for x in fruits:
    if 'a' in x:
        newlist.append(x)


print(*newlist)
'''

# [newlist.append(x) for x in fruits if 'a' in x]
# print(newlist)

[newlist.append(x) for x in fruits if x != 'apple']
newlist.sort(reverse=True)
# print(newlist)


markList = [100, 40, 60, 44, 55, 53, 50, 37, 99]
def findClose(number):
    return abs(number-50)
markList.sort(key = findClose)
print(markList)
