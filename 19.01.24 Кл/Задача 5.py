n = int(input('Введите натуральное число:\n'))
dig = ''
while n > 0:
    t_dig = n % 10
    n //= 10
    if dig == t_dig:
        print('Да.')
        break
    dig = t_dig
else:
    print('Нет.')