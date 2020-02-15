s1 = input()
a = list(map(int, s1.split()))
dp = [0] * len(a)
dp[0] = 1
for i in range(len(a)):
    mx = 0
    for j in range(i):
        if a[i] % a[j] == 0 and dp[j] > mx:
            mx = dp[j]
        dp[i] = mx + 1

print(max(dp))
