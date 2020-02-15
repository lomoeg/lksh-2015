w, h, n = map(int, input().split())
k = 1
left, right = -1, w * n
while right - left > 1:
    metres = (left + right) // 2
    if (metres // w) * (metres // h) >= n:
        right = metres
    else:
        left = metres

print(right)