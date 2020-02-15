fin = open('dust.in')
n, w = list(map(int, fin.readline().split()))
cost = [0] * n
weight = [0] * n
pcv = [0] * n

for i in range(n):
    l = list(map(int, fin.readline().split()))
    cost[i] = l[0]
    weight[i] = l[1]
    pcv[i] = l[0] / l[1]

fout = open('dust.out', 'w')
costfinal = 0
while len(cost) != 0 and w > 0:
    i = pcv.index(max(pcv))
    if weight[i] <= w:
        costfinal += cost[i]
        w -= weight[i]
        del cost[i]
        del weight[i]
        del pcv[i]
    else:
        costfinal += cost[i] * (w / weight[i])
        break

print(costfinal, file= fout)
fin.close()
fout.close()