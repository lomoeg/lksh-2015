s = int(input())
cost = [0] + list(map(int, input().split()))
dp = [[0] * (s + 1) for i in range(len(cost) + 1)]
for i in range(1, len(cost)):
    for j in range(1, s + 1):
        if j >= cost[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i]] + cost[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[len(cost) - 1][s])