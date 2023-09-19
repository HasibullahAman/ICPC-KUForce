result_list = []
number_of_testCase = int(input("Enter the number of test case: "))
for _ in range(number_of_testCase):
    alpha_list = []
    favrit_word = set()
    def check():
        for i in range(len(alpha_list)):
            fov_word = alpha_list[i]
            my_word = 'vika'
            for x in range(len(fov_word)):
                if fov_word[x] == my_word[x]:
                    favrit_word.add(fov_word[x])

    size = list(map(int, input('Enter the size of Carpet: ').split()))
    for y in range(0, size[0]):
        alpha_list.append(input("Enter the word: "))
    check()
    for i in range(number_of_testCase):
        if len(favrit_word) == 4:
            result_list.append("Yes")
        else:
            result_list.append("No")

print(*result_list)



