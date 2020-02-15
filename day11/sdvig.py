n = int(input())

count_plus = 0
count_minus = 0
a = []

for i in range(n):
    x, y = map(int, input().split())
    if x > 0:
        count_plus+=1
    else:
        count_minus+=1

if (count_plus <= 1) | (count_minus <= 1):
    print("Yes")
else:
    print("No");