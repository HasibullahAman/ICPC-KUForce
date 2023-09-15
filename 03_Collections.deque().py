from collections import deque

d = deque()
for i in range(int(input())):
    inp = input()
    if inp == 'pop':
        d.pop()
    elif inp == 'popleft':
        d.popleft()
    else:
        commend, value = inp.split()
        if commend == 'append':
            d.append(value)
        else:
            d.appendleft(value)

print(*d)
