def generate(k, prefix):
    if k == 0:
        print(*prefix, file = f1)
    else:
        for i in range(n, 0, -1):
            if i not in prefix:
                prefix.append(i)
                generate(k - 1, prefix)
                prefix.pop()


f = open('permutations.in')
n = int(f.readline())
f.close()

f1 = open('permutations.out', 'w')
generate(n, [])
f1.close()