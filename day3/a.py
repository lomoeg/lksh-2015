n = int(input())

s1 = input()
collection = list(map(int, s1.split()))

m = int(input())

s2 = input()
numbers = list(map(int, s2.split()))

for i in range(m):
    left, right = -1, len(collection)
    while right - left > 1:
        medium = (left + right) // 2
        if collection[medium] <= numbers[i]:
            left = medium
        else:
            right = medium
    if left != -1 and collection[left] == numbers[i]:
        print('YES')
    else:
        print('NO')