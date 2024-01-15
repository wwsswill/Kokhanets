import random

results = []

for _ in range(3):
    result = random.randint(1, 6)
    results.append(str(result))

number = int("".join(results))

square = number ** 2

print("Выпало очков:")
print(*results, sep=" ")
print("Число:", number)
print("Его квадрат:", square)

