def f(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return f(n // 8) + n % 8
    else:
        return f(n // 8)


c = 0
for n in range(8**6, 8**7+1):
    if f(n) == 2:
        c += 1
print(c)
