fin = open('father.in')
fout = open('father.out', 'w')

n = int(fin.readline())
a = list(map(int, fin.readline().split()))
c = [[0] * n for i in range(n)]
for i in range(1, n):
    c[a[i - 1] - 1][i] = 1
    c[i][a[i - 1] - 1] = 1

#print(c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            c[i][j] = min(c[i][j], c[i][k] + c[k][j])


for i in range(n):
    for j in range(n):
        print(c[i][j], file=fout, end=' ')
    print(file=fout)

fin.close()
fout.close()