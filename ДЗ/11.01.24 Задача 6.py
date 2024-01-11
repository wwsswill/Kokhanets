number = int(input('Введите четырёхзначное число: '))
thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10
print(number)
print(thousands)
print(hundreds)
print(tens)
print(units)
