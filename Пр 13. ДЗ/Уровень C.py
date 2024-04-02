import random

ar = [random.randint(2, 100) for _ in range(5)]


def prim(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        return True


prim_numbers = [num for num in ar if prim(num)]
aver_prim = sum(prim_numbers) / len(prim_numbers) if prim_numbers else 0

print("Массив:")
print(' '.join(map(str, ar)))
print("Простые числа:")
print(' '.join(map(str, prim_numbers)))
print(f"Среднее арифметическое: {aver_prim}")