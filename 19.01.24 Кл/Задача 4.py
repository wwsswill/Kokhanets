num = int(input('Введите натуральное число:\n'))
sum_of_digits = 0
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10
print("Сумма цифр", sum_of_digits)