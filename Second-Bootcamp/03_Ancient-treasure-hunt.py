# Function to find the length of the longest shared path between two scrolls
def longest_shared_path(scroll1, scroll2):
    # Create a dynamic programming table
    dp = [[0] * (len(scroll2) + 1) for _ in range(len(scroll1) + 1)]

    # Iterate through the scrolls and update the table
    for i in range(len(scroll1) - 1, -1, -1):
        for j in range(len(scroll2) - 1, -1, -1):
            if scroll1[i] == scroll2[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1

    # Find the maximum value in the table
    max_length = max(max(row) for row in dp)

    return max_length


# Read the number of test cases
num_test_cases = int(input())

# Iterate through each test case
for _ in range(num_test_cases):
    # Read the scrolls' inscriptions
    scroll1 = input()
    scroll2 = input()

    # Find the length of the longest shared path
    longest_path = longest_shared_path(scroll1, scroll2)

    # Print the result
    print(longest_path)