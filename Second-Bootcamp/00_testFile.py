def subset_sum(arr, target):
    n = len(arr)
    # print(arr)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    # print(dp)
    for i in range(n + 1):
        dp[i][0] = True

num_test_cases = int(input())
arr = []
target = 0
# Iterate through each test case
for _ in range(num_test_cases):
    # Read the number of elements in the array
    n = int(input())

    # Read the array elements
    arr = list(map(int, input().split()))

    # Read the target sum
    target = int(input())

    # # Check if there exists a subset with the given sum
    # if subset_sum(arr, target):
    #     print("Yes")
    # else:
    #     print("No")

subset_sum(arr, target)