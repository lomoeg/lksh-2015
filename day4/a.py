s1 = input()
s = list(map(int, s1.split()))
n = int(s[0])
k = int(s[1])

dp = [1]
for i in range(k):
    dp.append(sum(dp))

for i in range(k + 1, n):
    dp.append(0)
    for x in range(i - k, i):
        dp[i] += dp[x]

#print(*dp)

print(dp[n - 1])