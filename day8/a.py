import operator

fin = open('frequency.in')
fout = open('frequency.out', 'w')
d = dict()
seq = fin.readline().split()
while len(seq) > 0:
    for i in range(len(seq)):
        if seq[i] not in d:
            d[seq[i]] = 1
        else:
            d[seq[i]] += 1
    seq = fin.readline().split()
result = []
for el in d:
    result.append((d[el], el))

result.sort()
print(*map(operator.itemgetter(1), result), sep="\n", file= fout)

#for el in range(len(result)):
#    print(result[el][1])
fin.close()
fout.close()
