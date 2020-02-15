def sum(a, b):
    if a <= b:
        print(a, end=" ")
        a += 1
        sum(a, b)
    return

s = input()
a1, b1 = map(int, s.split())
sum(a1, b1)