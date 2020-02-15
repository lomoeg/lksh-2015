INF = float('inf')
fin = open('distance.in')
fout = open('distance.out', 'w')
n, m = map(int, fin.readline().split())
s, f = map(int, fin.readline().split())
graph = [{} for i in range(n )]
for i in range(n):
    for j in range(n):
        graph[i][j] = INF

for i in range(m):
    b, e, w = map(int, fin.readline().split())
    graph[b - 1][e - 1] = w
    graph[e - 1][b - 1] = w

par = [[0] * n]
D = set()
d = [[INF] for i in range(n)]
d[s - 1] = 0
for i in range(n):
    mn = INF
    for v in range(n):
        if v not in D and d[v] < mn:
            mn = d[v]
            vmn = v
    if mn == INF:
        break
    D.add(vmn)
    #print(vmn)
    for u, w in graph[vmn].items():
        d[u] = min(d[u], d[vmn] + w)
        if d[vmn] + w < d[u]:
            d[u] = d[vmn] + w
            #print(u, w)
            par[u] = vmn

print(par)
if d[f - 1] == INF:
    print(-1, file=fout)
else:
    print(d[f - 1], file=fout)
fin.close()
fout.close()
