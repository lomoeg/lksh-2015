fin = open('football.in')
fout = open('football.out', 'w')
n, k = map(int, fin.readline().split())
dp = [[0] * (n + 1) for i in range(k + 1)]
dp[1][0] = 1
dp[1][1] = 1
dp[1][3] = 1

for i in range(1, k + 1):
    dp[i][0] = 1
#print(dp)
for i in range(2, k + 1):
    for j in range(1, n + 1):
        if j > 3:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j - 3] + dp[i - 1][j]
print(dp)
print(dp[k][n])

fin.close()
fout.close()