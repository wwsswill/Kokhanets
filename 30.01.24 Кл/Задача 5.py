s = ''
a, b = map(int, input('Введите границы диапазона:\n').split())
for i in range(a, b + 1):
    k = 0
    for j in range(2, i):
        if i % j == 0:
            k += 1
        if k > 2:
            break
    if k == 2:
        s += str(i) + ' '
print(', '.join(i for i in s.split()))