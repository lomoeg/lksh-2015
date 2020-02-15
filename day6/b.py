def generate(k, prefix):
    if k == 0:
        print(*prefix, file = f1)
    else:

        prefix.append(0)
        generate(k - 1, prefix)
        prefix.pop()

        if prefix == []:
            prefix.append(1)
            generate(k - 1, prefix)
            prefix.pop()
        elif prefix[-1] != 1:
            prefix.append(1)
            generate(k - 1, prefix)
            prefix.pop()


f = open('fibseq.in')
n = int(f.readline())
f.close()

f1 = open('fibseq.out', 'w')
generate(n, [])
f1.close()
