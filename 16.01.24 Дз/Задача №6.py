a, b, v = [int(i) for i in input('Введите возраст мальчиков: ').split()]
print(f'Возраст Антона: {a}')
print(f'Возраст Бориса: {b}')
print(f'Возраст Виктора: {v}')
if a > b and a > v:
    print('Антон старше всех')
elif b > a and b > v:
    print('Борис старше всех')
elif v > a and v > b:
    print('Виктор старше всех')
elif a == b and b > v and a > v:
    print(f'Антон Борис старше Виктора')
elif a == v and v > b and a > b:
    print(f'Антон и Виктор старше Бориса')
elif a == b and a == v and b == v and b == a and v == a and v == b:
    print('Мальчики одного возраста')
else:
    print(f'Борис и Виктор старше Антона')