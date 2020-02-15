const = 137
n = input()
s1 = input()
seq = list(map(int, s1.split()))

one = seq[0]
for i in range(len(seq)):
    seq[i] -= one

counts = [0] * (const * 2 + 1)

for el in seq:
    counts[el + const] += 1

result = []

for i in range(len(counts)):
    result += [i + one - const] * counts[i]

print(*result)