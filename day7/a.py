def nextcomb(comb, n):
    new_comb = comb
    i = len(comb) - 1
    while i >= 0 and comb[i] == n - len(comb) + i + 1:
        i -= 1
    if i < 0:
        return [0]
    new_comb[i] += 1
    new_comb[i + 1:] = list(range(new_comb[i] + 1, new_comb[i] + len(comb) - i))
    return new_comb


f = open('nextcomb.in')
N, K = map(int, f.readline().split())
comb1 = list(map(int, f.readline().split()))
f.close()
f1 = open('nextcomb.out', 'w')
print(*nextcomb(comb1, N), file = f1)
f1.close()
