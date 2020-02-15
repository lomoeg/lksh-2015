fin = open('mindist.in')
fout = open('mindist.out', 'w')
n, m = map(int, fin.readline().split())
graph = [list(map(int, fin.readline().split())) for i in range(n)]
queue = [m]
dist = {m: 0}

graph1 = [set() for i in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            graph1[i].add(j + 1)

for u in queue:
    for v in graph1[u - 1]:
        if v not in dist:
            dist[v] = dist[u] + 1
            queue.append(v)
res = []
for i in range(n):
    res.append(dist.get(i + 1, -1))
print(*res, file=fout)
print(*graph1)
fin.close()
fout.close()