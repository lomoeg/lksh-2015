p = 179
M = int(1e9 + 7)

f_in = open('eqsubstr.in')
seq = f_in.readline()
Q = int(f_in.readline())
powers = [1]
for i in range(len(seq)):
    powers.append(powers[-1] * p % M)

prefixes = [0]
for ch in seq:
    prefixes.append((prefixes[-1] * p + ord(ch) - ord('a') + 1) % M)


def substr_hash(i, j):
    return (prefixes[j] - prefixes[i - 1] * powers[j - i + 1]) % M


f_out = open('eqsubstr.out', 'w')

for i in range(Q):
    l1, r1, l2, r2 = map(int, f_in.readline().split())
    if substr_hash(l1, r1) == substr_hash(l2, r2):
        print('+', end='', file=f_out)
    else:
        print('-', end='', file=f_out)

f_in.close()
f_out.close()