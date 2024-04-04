import random

array = [random.randint(0, 5) for _ in range(5)]

min_e = min(array)
min_in = array.index(min_e) + 1
max_e = max(array)
max_in = array.index(max_e) + 1

print("Массив:")
print(" ".join(map(str, array)))
print(f"Минимальный элемент: A[{min_in}]={min_e}")
print(f"Максимальный элемент: A[{max_in}]={max_e}")