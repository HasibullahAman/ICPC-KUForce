def three():
    printNumber = []
    for _ in range(int(input())):
        number = int(input("Enter the number of we find: "))
        def threeFib(number):
            if number == 0:
                return 0
            elif number == 1:
                return 1
            elif number == 2:
                return 1
            else:
                return threeFib(number - 1) + threeFib(number - 2) + threeFib(number - 3)
        printNumber.append(threeFib(number))
    for i in printNumber:
        print(i)


%timeit three()