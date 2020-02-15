INF = float('inf')


def dijkstra():
    current = n
    for j in range(n):
        if d[j] <= d[current] and not used[j]:
            current = j
    used[current] = True
    for j in edges[current]:
        if d[j] > d[current] + edges[current][j]:
            d[j] = d[current] + edges[current][j]
            prev[j] = current    


fin = open('distance.in')
n, m = map(int, fin.readline().strip().split())
s, f = map(int, fin.readline().strip().split())
s -= 1
f -= 1

edges = [{} for i in range(n)]
for i in range(m):
    a, b, c = map(int, fin.readline().strip().split())
    edges[a - 1][b - 1] = c
    edges[b - 1][a - 1] = c

d = [INF] * (n + 1)
prev = [None] * n
used = [False] * n
d[s] = 0

for i in range(n):
    dijkstra()
print(d)
fout = open('distance.out', 'w')
if d[f] != INF:
    fout.write(str(d[f]) + '\n')
    answer = []
    j = f
    while j != None:
        answer.append(j + 1)
        j = prev[j]
    fout.write(' '.join(map(str, reversed(answer))))
else:
    fout.write('-1')
fin.close()
fout.close()