numbers = input('Введите три числа: ').split()
if numbers[0] == numbers[1] == numbers[2]:
    print('Все числа одинаковые.')
elif numbers[0] == numbers[1] or numbers[0] == numbers[2] or numbers[1] == numbers[2]:
    print('Два числа одинаковые.')
else:
    print('Нет одинаковых чисел.')