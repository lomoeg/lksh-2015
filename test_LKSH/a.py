fin = open('divisors.in')
fout = open('divisors.out', 'w')


def prime(n):
    num = n
    i = 2
    s = []
    if n != 1:
        while ceil(sqrt(num)) >= i:
            while n % i == 0:
                n //= i
                s.append(i)
            i += 1
    if not s or n != 1:
        s.append(n)
    s1 = list(map(int, s))
    return s1


from math import *
d = dict()
n = int(fin.readline())
arr = list(map(int, fin.readline().split()))

for i in arr:
    count = 0
    for i in prime(i):
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

print(len(d), file=fout)
#print(d)
res = []
for i, j in d.items():
    res.append([j, i])

res.sort()
for i in range(len(res)):
    print(*reversed(res[i]), file=fout)
#print(res)
fin.close()
fout.close()