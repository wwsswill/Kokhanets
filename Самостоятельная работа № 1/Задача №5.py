def F(n):
    if n == 0:
        return 1
    elif n % 2 != 0:
        return F(n // 100) * (n % 10)
    elif n > 0 and n % 2 == 0:
        return F(n // 100)


c = 0
for n in range(10 ** 9, 6 * 10 ** 9 + 1):
    if F(n) == 21:
        c += 1
print(c)
