import sys


def dfs(v, color):
    used[v] = color
    new_color = 3 - color
    for u in graph[v]:
        if used[u] == 0:
            if not dfs(u, new_color):
                return False
        elif used[v] == used[u]:
            return False
    return True


sys.setrecursionlimit(10 ** 6)

fin = open('bipartite.in')
fout = open('bipartite.out', 'w')
n, m = map(int, fin.readline().split())
graph = [[] for i in range(n)]
for i in range(m):
    a, b = list(map(int, fin.readline().split()))
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

used = [0] * n

res = True
for v in range(n):
    if used[v] == 0 and not dfs(v, 1):
        res = False
        break

if res:
    print('YES', file=fout)
else:
    print('NO', file=fout)

fin.close()
fout.close()