from sys import setrecursionlimit

setrecursionlimit(10 ** 6)
fin = open('matrix2.in')
fout = open('matrix2.out', 'w')
n, m = map(int, fin.readline().split())
graph = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, fin.readline().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

used = [0] * n


def dfs(v, component):
    component.append(v + 1)
    used[v] = 1
    for u in graph[v]:
        if not used[u]:
            dfs(u, component)


components = []
for v in range(n):
    if not used[v]:
        components.append([])
        dfs(v, components[-1])

print(len(components), file=fout)
for i in range(len(components)):
    print(len(components[i]), file=fout)
    print(*components[i], file=fout)

fin.close()
fout.close()

