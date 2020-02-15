s1 = input()
n, m = list(map(int, s1.split()))

matrix = [[0] * (m + 1) for i in range(n + 1)]

for i in range(m + 1):
    matrix[n][i] = 10**9

for i in range(n + 1):
    matrix[i][m] = 10**9

#print(*matrix)
# n строчек, m  столбцов

for i in range(n):
    s2 = input()
    s = list(map(int, s2.split()))
    matrix[i] = s

