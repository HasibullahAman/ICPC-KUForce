for test_case in range(int(input("Enter the number of TestCase: "))):
    length_of_Array = int(input("Enter the length of Array: "))
    array_list = list(map(int, input("Enter the element of Array: ")))
    smallest_missing = 1
    while smallest_missing in array_list:
        smallest_missing += 1
    print(smallest_missing)