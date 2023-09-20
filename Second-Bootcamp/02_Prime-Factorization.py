
final_output = []
for _ in range(int(input("Enter the number of test Case: "))):
    result_list = []
    number = int(input("Enter the number for finding the prime Factorization: "))
    for i in range(2, number + 1):
        while number % i == 0:
            result_list.append(i)
            number = number // i
    final_output.append(result_list)
for i in final_output:
    print(*i)