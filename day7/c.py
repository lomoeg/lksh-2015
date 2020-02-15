from math import factorial


def perm_by_index(n, idx):
    notused = list(range(1, n + 1))
    block = factorial(n - 1)
    result = []
    for i in range(n):
        block_idx = idx // block
        result.append(notused[block_idx])
        notused.pop(block_idx)
        idx %= block
        if i < n - 1:
            block //= n - i - 1
    return result


f_in = open('bynumber.in')
N = int(f_in.readline())
number = int(f_in.readline())
f_in.close()
f_out = open('bynumber.out', 'w')
print(*perm_by_index(N, number), file = f_out)
f_out.close()

