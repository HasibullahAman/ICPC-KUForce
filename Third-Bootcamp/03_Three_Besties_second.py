# # Dictionary to store already computed values
# memo = {}
# def threeFib(number):
#     if number in memo:
#         return memo[number]
#     if number == 0:
#         result = 0
#     elif number == 1:
#         result = 1
#     elif number == 2:
#         result = 1
#     else:
#         result = threeFib(number - 1) + threeFib(number - 2) + threeFib(number - 3)
#     memo[number] = result
#     return result
#
# printNumber = []
# num_test_cases = int(input("Enter the number of test cases: "))
# for _ in range(num_test_cases):
#     number = int(input("Enter the number to find in the threeFib sequence: "))
#     printNumber.append(threeFib(number))
# for i in printNumber:
#     print(i)

notcheck = {}
def ThreeFib(number):
    if number in notcheck:
        return notcheck[number]
    elif number == 0:
        result = 0
    elif number == 1:
        result = 1
    elif number ==  2:
        result = 1
    else:
        result = ThreeFib(number - 1) + ThreeFib(number - 2) + ThreeFib(number- 3)
    notcheck[number] = result
    return result

printNumber = []
for _ in range(int(input("Enter the number of test case: "))):
    number = int(input("Enter the number: "))
    printNumber.append(ThreeFib(number))

for i in printNumber:
    print(i)
