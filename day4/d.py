s1 = input()
n, m = list(map(int, s1.split()))
invariant = [[-2, 1], [-1, -2], [-2, -1], [1, -2]]

if m > n:
    n, m = m, n

dp = [[0] * (m + 4) for i in range(n + 4)]
dp[2][2] = 1

for i in range(2, (n + 2) * 2):
    for j in range(i):
        x = i - j - 1
        y = j
        if x in range(2, n + 2) and y in range(2, m + 2):
            for u in range(len(invariant)):
                dp[x][y] += dp[x + invariant[u][1]][y + invariant[u][0]]

print(dp[n + 1][m + 1])