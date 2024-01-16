age = int(input('Введите возраст: '))
if age > 120:
    print('Введён слишком большой возраст')
elif age == 1 or age % 10 == 1 and age != 11:
    print(f'Вам {age} год')
elif age == 2 or age % 10 == 2 and age != 12:
    print(f'Вам {age} года')
elif age == 3 or age % 10 == 4 and age != 13:
    print(f'Вам {age} года')
elif age == 4 or age % 10 == 4 and age != 14:
    print(f'Ваи {age} года')
else:
    print(f'Вам {age} лет')
