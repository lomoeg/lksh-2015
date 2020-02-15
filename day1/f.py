n = int(input())

s1 = input()
pupils = list(map(int, s1.split()))

pupils.sort()

print(pupils[len(pupils) - n])
