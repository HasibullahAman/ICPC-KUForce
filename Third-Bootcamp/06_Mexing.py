def calculate_mex(arr):
    mex = 0
    while mex in arr:
        mex += 1
    return mex

# Read inputs
n = int(input())
m = int(input())
arr = []
for _ in range(m):
    a, b = map(int, input().split())
    arr.append([a, b])

# Initialize mex array
mex = [[0] * n for _ in range(2)]

# Calculate mex values
for i in range(n):
    mex[0][i] = calculate_mex(mex[1][i])

# Print mex values
for i in range(n):
    print(mex[0][i], end=' ')
