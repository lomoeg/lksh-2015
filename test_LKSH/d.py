a = list(map(int, input().split()))
d = dict()
res = 0
for i in a:
    d[i] = 0

for i in a:
    d[i] += 1

for i, j in d.items():
    d[i] = i * j
mx = - 1000000
for i, j in d.items():
    if j >= mx:
        mx = j
        res = i

#val = max(d.values())
#res = max(d.keys())
print(res, d)
