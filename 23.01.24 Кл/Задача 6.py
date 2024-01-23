start = int(input("Введите начало отрезка: "))
end = int(input("Введите конец отрезка: "))
step = int(input("Введите шаг: "))


def calculate_function(x):
    return x ** 3 + 2 * x ** 2 - 4 * x + 1


for x in range(end, start - 1, step):
    y = calculate_function(x)
    print(f"В точе {x} функция равна {y}")
