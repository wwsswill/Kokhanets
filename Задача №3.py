import random
number = random.randint(100, 999)
hundreds = number // 100
tens = (number // 10) % 10
units = number % 10
print('Получено число:', number)
print('сотни:', hundreds)
print('десятки:', tens)
print('единицы:', units)
