def generate(k, prefix):
    if k == 0:
        print(*prefix, file = f1)
    else:
        for i in range(K):
            prefix.append(i)
            generate(k - 1, prefix)
            prefix.pop()


f = open('numbers.in')
N, K = map(int, f.readline().split())
f.close()

f1 = open('numbers.out', 'w')
generate(N, [])
f1.close()