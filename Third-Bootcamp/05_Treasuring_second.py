n, W = map(int, input().split())
treasures = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (W + 1)

for weight, value in treasures:
    print(weight)
    print(value)
    for w in range(W, weight - 1, -1):
        print(w)
        dp[w] = max(dp[w], value + dp[w - weight])
    print(dp[w])
    breakpoint()

print(dp[W])

















