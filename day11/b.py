import sys


def dfs(v):
    used[v] = True
    for u in range(len(graph[v])):
        if graph[v][u] == 1 and not used[u]:
            dfs(u)


sys.setrecursionlimit(10 ** 6)

fin = open('tree.in')
fout = open('tree.out', 'w')
n = int(fin.readline())
graph = [list(map(int, fin.readline().split())) for i in range(n)]
m = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            m += 1
m //= 2
used = [0] * n

res = True
count = 0

for v in range(n):
    if not used[v]:
        dfs(v)
        count += 1

if m != n - 1 or count > 1:
    res = False

if res:
    print('YES', file=fout)
else:
    print('NO', file=fout)

fin.close()
fout.close()