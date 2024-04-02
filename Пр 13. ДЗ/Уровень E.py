import random

n = int(input("Введите количество элементов "))
A = [random.randint(1, 100) for _ in range(n)]
sum_A = n * (n + 1) // 2
print("Массив")
print(' '.join(map(str, A)))
print(f"Знакопеременную сумма {sum_A}")
