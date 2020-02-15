fin = open('hemoglobin.in')
fout = open('hemoglobin.out', 'w')


n = int(fin.readline())
a = [0]
sum = [0]
for i in range(n):
    seq = fin.readline()
    if seq[0] == '+':
        a.append(int(seq[1:]))
        sum.append(sum[-1] + a[-1])
    elif seq[0] == '?':
        res = 0
        res = sum[-1] - sum[len(sum) - 1 - int(seq[1:])]
        print(res, file=fout)
    else:
        sum.pop()
        print(a.pop(), file=fout)

fin.close()
fout.close()