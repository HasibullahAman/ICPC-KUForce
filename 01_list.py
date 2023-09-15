"""
print
pop
sort
reverse
----------------
append e
remove e
-----------
insert e i
"""

my_list = []
for i in range(int(input())):
    commend = input()
    if commend == 'print':
        print(my_list)
    elif commend == 'pop':
        my_list.pop()
    elif commend == 'sort':
        my_list.sort()
    elif commend == 'reverse':
        my_list.reverse()
    else:
        try:
            commend, value = commend.split()
            if commend == 'append':
                my_list.append(int(value))
            elif commend == 'remove':
                my_list.remove(int(value))
        except:
            commend, value, index = commend.split()
            my_list.insert(int(value), int(index))
