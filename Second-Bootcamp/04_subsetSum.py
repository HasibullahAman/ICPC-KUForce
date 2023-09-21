def subset_sum(arr, target, n, memo):
    # Base cases
    if target == 0:
        return True
    if n == 0:
        return False

    # Check if the subproblem has already been solved
    if memo[n][target] != -1:
        return memo[n][target]

    # If the last element is greater than the target, exclude it
    if arr[n - 1] > target:
        memo[n][target] = subset_sum(arr, target, n - 1, memo)
        return memo[n][target]

    # Recursively check if the target can be achieved either by including or excluding the last element
    memo[n][target] = subset_sum(arr, target - arr[n - 1], n - 1, memo) or subset_sum(arr, target, n - 1, memo)
    return memo[n][target]


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

    # Initialize memoization table with -1 values
    memo = [[-1] * (target + 1) for _ in range(n + 1)]

    # Check if there exists a subset with the given sum
    if subset_sum(arr, target, n, memo):
        print("Yes")
    else:
        print("No")