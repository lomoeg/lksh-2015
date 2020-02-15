import random
fin = open('qsort.in')
fout = open('qsort.out', 'w')


def qsort(seq):
    if len(seq) > 1:
        x = random.choice(seq)
        less = qsort([el for el in seq if el < x])
        more = qsort([el for el in seq if el > x])
        seq = less + [x] * (len(seq) - len(less) - len(more)) + more
    return seq


a = list(map(int, fin.readline().split()))
print(*qsort(a), file=fout)
fin.close()
fout.close()