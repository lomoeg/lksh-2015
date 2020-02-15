fin = open('floyd.in')
fout = open('floyd.out', 'w')
n = int(fin.readline())
c = [list(map(int, fin.readline().split())) for i in range(n)]

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