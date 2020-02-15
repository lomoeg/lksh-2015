infinity = 10 ** 7 + 1
fin = open('dijkstra.in')
fout = open('dijkstra.out', 'w')
n, s, f = map(int, fin.readline().split())
graph = [{} for i in range(n)]
for i in range(n):
    l = list(map(int, fin.readline().split()))
    for j in range(n):
        if l[j] == -1:
            graph[i][j] = infinity
        else:
            graph[i][j] = l[j]
print(graph)
D = set()
d = [infinity for i in range(n)]
d[s - 1] = 0
for i in range(n):
    mn = infinity
    for v in range(n):
        if v not in D and d[v] < mn:
            mn = d[v]
            vmn = v
    if mn == infinity:
        break
    D.add(vmn)
    for u, w in graph[vmn].items():
        d[u] = min(d[u], d[vmn] + w)

if d[f - 1] == infinity:
    print(-1, file=fout)
else:
    print(d[f - 1], file=fout)
fin.close()
fout.close()