n = int(input())

s1 = input()
pupils = list(enumerate(map(int, s1.split())))

for i in range(len(pupils) - 1):
    changed = False
    for j in range(n - i - 1):
        if pupils[j][1] < pupils[j + 1][1]:
            pupils[j], pupils[j + 1] = pupils[j + 1], pupils[j]
            changed = True
    if not changed:
        break


print(*[i + 1 for i, x in pupils])

