def prime(n):
    num = n
    i = 2
    s = []
    if n != 1:
        while ceil(sqrt(num)) >= i:
            while n % i == 0:
                n //= i
                s.append(i)
            i += 1
    if not s or n != 1:
        s.append(n)
    s1 = list(map(int, s))
    return s1

from math import *

k = int(input())

print(prime(k))