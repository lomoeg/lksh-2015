fin = open('components.in')
fout = open('components.out', 'w')
n = int(fin.readline())
graph = [list(map(int, fin.readline().split())) for i in range(n)]
used = [0] * n


def dfs(v, component):
    component.append(v)
    used[v] = 1
    for u in range(len(graph[v])):
        if graph[v][u] == 1 and not used[u]:
            dfs(u, component)


components = []
for v in range(n):
    if not used[v]:
        components.append([])
        dfs(v, components[-1])

print(len(components), file=fout)
fin.close()
fout.close()
