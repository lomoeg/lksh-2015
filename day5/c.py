s1 = input()
a = list(map(int, s1.split()))
s2 = input()
b = list(map(int, s2.split()))

dp = [[0] * (len(b) + 1) for i in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] != b[j - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        else:
            dp[i][j] = dp[i - 1][j - 1] + 1

print(dp[len(a)][len(b)])
result = []

i, j = len(a), len(b)
while i > 0 and j > 0:
    if a[i - 1] == b[j - 1]:
        result.append(a[i - 1])
        i -= 1
        j -= 1
    elif dp[i][j - 1] > dp[i - 1][j]:
        j -= 1
    else:
        i -= 1

print(*reversed(result))
