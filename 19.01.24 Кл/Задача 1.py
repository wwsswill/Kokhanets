A, B = map(int, input('Введите два целых числа:\n').split())
for i in range(A, B + 1):
    print(f"{i}*{i}={i * i}")
