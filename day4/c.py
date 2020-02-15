s1 = input()
n, m = list(map(int, s1.split()))

# n - строка, m -  столбец
# начинаем с (2, 2) до (n + 2, m + 2)

dp = [[0] * (n + 2) for i in range(m + 2)]

dp[2][2] = 1

for j in range(2, n + 2):
    for i in range(2, m + 2):
        dp[i][j] = dp[i][j] + dp[i - 1][j - 2] + dp[i - 2][j - 1]


print(dp[m + 1][n + 1])

