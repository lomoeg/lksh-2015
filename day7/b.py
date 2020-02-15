def lastcomb(comb):
    new_comb = comb
    i = len(comb) - 1
    while i >= 1 and comb[i] >= comb[i - 1]:
        i -= 1
    if i == 0:
        return reversed(comb)
    mx = 0
    for j in range(i, len(new_comb)):
        if new_comb[j] <= new_comb[i - 1] and new_comb[j] > mx:
            mx = new_comb[j]
    new_comb[new_comb.index(mx)], new_comb[i - 1] = comb[i - 1], new_comb[new_comb.index(mx)]
    new_comb[i:] = reversed(sorted(new_comb[i:]))
    return new_comb


f = open('prev.in')
N = int(f.readline())
comb1 = list(map(int, f.readline().split()))
f.close()
f1 = open('prev.out', 'w')
print(*lastcomb(comb1), file = f1)
f1.close()
