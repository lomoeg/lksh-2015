fin = open('dictionary.in')
fout = open('dictionary.out', 'w')
d = {}
l = list(map(str.rsplit, fin.readlines()))
line = []
for i in l:
    line += list(i)
for i in range(len(line)):
    if line[i][-1] == ',':
        line[i] = line[i][:-1]
line.append(' ')
line.append(' ')

for i in range(len(line) - 1):
    if line[i + 1] == '-' and i + 1 < len(line):
        j = i + 2
        while line[j + 1] != '-' and j + 2 < len(line):
            if line[j] in d:
                d[line[j]] += ([line[i]])
            else:
                d[line[j]] = [line[i]]
            j += 1
        i = j - 2

print(len(d), file=fout)
for key in sorted(d):
    print(key, '-', ', '.join(d[key]), file=fout)
fin.close()
fout.close()
