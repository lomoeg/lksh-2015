def cars(n):
    result = 0
    if n > k:
        result += cars(n // 2)
        result += cars(n - n // 2)
    else:
        result += 1
    return result


s1 = input()
n, k = map(int, s1.split())

print(cars(n))