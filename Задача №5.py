a, b, c, d, e = [int(i) for i in input('Введите пять целых чисел:').split()]
if a > b and a > c and a > d and a > e:
    m = a
elif b > a and b > c and b > d and b > e:
    m = b
elif c > a and c > b and c > d and c > e:
    m = c
elif d > a and d > b and d > c and d > e:
    m = d
else:
    m = e
print(f'Максимальное число {m}')
