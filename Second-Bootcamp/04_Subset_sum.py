# result_list = []
#
# for _ in range(int(input("Enter the number of test case: "))):
#     numberOfElement = int(input("Enter the number of array element:"))
#     arrayOfNumber = list(map(int, input().split())).sort()
#     target = int(input("Enter the target: "))
#


# Function to check if there exists a subset with the given sum
def subset_sum(arr, target):
    n = len(arr)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # If the target sum is 0, it can be achieved by selecting an empty subset
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

    return dp[n][target]

# Read the number of test cases
num_test_cases = int(input())

# Iterate through each test case
for _ in range(num_test_cases):
    # Read the number of elements in the array
    n = int(input())

    # Read the array elements
    arr = list(map(int, input().split()))

    # Read the target sum
    target = int(input())

    # Check if there exists a subset with the given sum
    if subset_sum(arr, target):
        print("Yes")
    else:
        print("No")