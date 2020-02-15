fin = open('min.in')
fout = open('min.out', 'w')

n, k = list(map(int, fin.readline().split()))
a = list(map(int, fin.readline().split()))
for i in range(n - k + 1):
    mn = min(a[i: i + k])
    print(mn, file=fout)
fin.close()
fout.close()