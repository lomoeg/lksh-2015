def generate(n, numbers, pr, count):
    if n == 0:
        if numbers == k:
            print(*pr, file=fout)
        return
    else:
        if k - numbers <= n:
            for i in range(1, k + 1):
                pr.append(i)
                if i in count:
                    changed = False
                else:
                    numbers += 1
                    changed = True
                count.add(i)
                generate(n - 1, numbers, pr, count)
                if changed:
                    count.discard(i)
                    numbers -= 1
                pr.pop()


fin = open('wishbox.in')
fout = open('wishbox.out', 'w')
k, n = map(int, fin.readline().split())
generate(n, 0, [], set())
fin.close()
fout.close()