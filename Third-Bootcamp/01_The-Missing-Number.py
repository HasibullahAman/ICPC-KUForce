outputList = []
for number_of_testCase in range(int(input("Enter te number of test Case: "))):
    length_ofArray = int(input("Enter the number of Element: "))
    start_ofArray = 0
    array_list = list(map(int, input("Enter the element of Array: ").split()))
    array_list = sorted(array_list)
    for check in range(0, len(array_list)):
        if start_ofArray == array_list[check]:
            start_ofArray += 1
        else:
            outputList.append(check)
            break
for i in outputList:
    print(i)

