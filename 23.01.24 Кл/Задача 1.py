numbers = []
for number in range(10000, 100000):
    if number % 133 == 125 and number % 134 == 111:
        numbers.append(number)
print('Пятизначные числа удовлетворяющие условиям:')
for number in numbers:
    print(number)
