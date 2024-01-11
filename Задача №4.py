a, b, c = [int(i) for i in input('Введите три целых числа:').split()]
if a > b and a > c:
    m = a
elif b > a and b > c:
    m = b
else:
    m = c
print(f'Максимальное число {m}')
