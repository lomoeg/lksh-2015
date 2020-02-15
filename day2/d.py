from collections import *

seq = input()
flag = True
a = []

scopeopen = '([{'
scopeclose = ')]}'

for i in range(len(seq)):
    if seq[i] in scopeopen:
        a.append(seq[i])
    elif not a or a[-1] != scopeopen[scopeclose.index(seq[i])]:
        flag = False
    else:
        a.pop()

if len(a) != 0:
    flag = False

if flag:
    print('YES')
else:
    print('NO')
