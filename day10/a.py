fin = open('reverse.in')
fout = open('reverse.out', 'w')
n = int(fin.readline())
graph = [list(map(int, fin.readline().split())) for i in range(n)]
graphres = [list() for i in range(n)]

for i in range(n):
    for x in graph[i]:
        graphres[x - 1].append(i + 1)

print(n, file=fout)
for i in range(n):
    print(*graphres[i], file=fout)
fin.close()
fout.close()