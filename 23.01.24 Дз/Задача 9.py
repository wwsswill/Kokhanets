x = int(input("Введите начальную сумму вклада: "))
y = int(input("Введите желаемую сумму вклада: "))
p = float(input("Введите процентную ставку: "))

years = 0

while x < y:
    x += x * p / 100
    x = int(x)
    years += 1

print("Количество лет:", years)
