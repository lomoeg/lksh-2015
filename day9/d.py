fin = open('priority-queue.in')
fout = open('priority-queue.out', 'w')


def add(heap, el):
    heap.append(el)
    idx = len(heap) - 1
    while idx > 1 and heap[idx] < heap[idx // 2]:
        heap[idx // 2], heap[idx] = heap[idx], heap[idx // 2]
        idx //= 2


def extraxt_max(heap):
    heap[1], heap[-1] = heap[-1], heap[1]
    extracted = heap.pop()
    idx = 1
    while 2 * idx < len(heap):
        pos = 2 * idx
        if 2 * idx + 1 < len(heap) and heap[2 * idx + 1] < heap[2 * idx]:
            pos = 2 * idx + 1
        if heap[pos] < heap[idx]:
            heap[pos], heap[idx] = heap[idx], heap[pos]
            idx = pos
        else:
            break
    return extracted


def minisort(heap):
    for i in range(2, len(heap)):
        idx = i
        while idx > 1 and heap[idx][1] > heap[idx // 2][1]:
            heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
            #d[seq[0]] = heap.index((seq[0], int(seq[1])))
            idx //= 2


    """for i in range(len(heap) - 1, 1, -1):
        heap[i], heap[1] = heap[i], heap[1]
        idx = 1
        while 2 * idx < i:
            pos = 2 * idx
            if 2 * idx + 1 < i and heap[2 * idx + 1][1] > heap[2 * idx][1]:
                pos = 2 * idx + 1
            if heap[pos][1] > heap[idx][1]:
                heap[pos], heap[idx] = heap[idx], heap[pos]
                idx = pos
            else:
                break
        print(heap)"""


def change(heap, seq):
    heap[d[seq[1]]][1] = seq[2]
    minisort(heap)


seq = fin.readline().split()
a = [()]
result = []
d = dict()
while len(seq) > 0:
    if seq[0] == 'ADD':
        del seq[0]
        a.append((seq[0], int(seq[1])))
        d[seq[0]] = a.index((seq[0], int(seq[1])))
        minisort(a)

    elif seq[0] == 'POP':
        result.append(extraxt_max(a))
    #else:
     #   change(a, seq)
    seq = fin.readline().split()

#print(d)
print(a)
print(*result)
fin.close()
fout.close()