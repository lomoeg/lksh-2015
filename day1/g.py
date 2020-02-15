s = input()

flag = True

for i in range(len(s)):

    if s[i: i + 2] == 'bb':
        flag = False
        break

    for x in range(1, len(s)):
        a = s[i: i + x]
        b = s[i + x: i + x * 2]
        c = s[i + x * 2: i + x * 3]
        if a == b and b == c:
            flag = False
            break

if flag:
    print('YES')
else:
    print('NO')