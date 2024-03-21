import random
A, B = map(int, input('Введите границы диапазона:\n').split())

mas = [random.randint(A, B) for _ in range(5)]
print('Массив:\n', mas)