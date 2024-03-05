def F(n):
    if n < 2:
        return n
    else:
        return F(n // 2) + F(n % 2)


count = 0

for n in range(2 ** 17):
    if F(n) == 27:
        count += 1
print(count)
