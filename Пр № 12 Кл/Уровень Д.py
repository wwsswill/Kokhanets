import random

n = int(input('Введите n:\n'))
mas = [i for i in range(1, n + 1)]

for i in range(n):
    j = random.randint(0, i)
    mas[i], mas[j] = mas[j], mas[i]

print('Массив:')
print(' '.join(map(str, mas)))