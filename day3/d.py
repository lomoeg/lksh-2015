n, k = map(int, input().split())
ropes = []
for i in range(n):
    ropes.append(int(input()))
left, right = 0, max(ropes) + 1
while right - left > 1:
    middle = (left + right) // 2
    res = 0
    for i in ropes:
        res += i // middle
    if res >= k:
        left = middle
    else:
        right = middle
print(left)