def metbefore(seq):
    s = set()
    len1 = len(s)
    for i in range(len(seq)):
        s.add(seq[i])
        if len(s) == len1:
            print('YES', file = f_out)
        else:
            len1 = len(s)
            print('NO', file = f_out)


f_in = open('metbefore.in')
seq1 = list(map(int, f_in.readline().split()))
f_in.close()
f_out = open('metbefore.out', 'w')
metbefore(seq1)
f_out.close()