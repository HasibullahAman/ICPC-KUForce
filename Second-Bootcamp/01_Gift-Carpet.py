import re
alpha_list = []
favrit_word = set()

def check():
    for i in range(len(alpha_list)):
        fov_word = alpha_list[i]
        my_word = 'vika'
        for x in range(len(fov_word)):
            if fov_word[x] == my_word[x]:
                favrit_word.add(fov_word[x])

for i in range(int(input("Enter the number of test case: "))):
    size = list(map(int, input('Enter the size of Carpet: ').split()))
    for y in range(0, size[0]):
        alpha_list.append(input("Enter the word: "))

check()

if len(favrit_word) == 4:
    print('Yes')
else:
    print("No")