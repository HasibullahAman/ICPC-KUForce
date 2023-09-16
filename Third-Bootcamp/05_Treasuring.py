def knapsack(n, W, weights, values):
    # Create a 2D table to store the maximum values
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    # Iterate through each treasure
    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]
        # Consider taking the current treasure
        for w in range(1, W + 1):
            if weight <= w:
                dp[i][w] = max(value + dp[i - 1][w - weight], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    # Return the maximum total value
    return dp[n][W]
# Read input
n, W = map(int, input().split())
weights = []
values = []

# Read weight and value of each treasure
for _ in range(n):
    weight, value = map(int, input().split())
    weights.append(weight)
    values.append(value)

# Call the knapsack function and print the result
result = knapsack(n, W, weights, values)
print(result)