def p_digits(number):
    digits = str(number)
    for digit in digits:
        print(digit)


number = int(input("Введите натуральное число: "))
p_digits(number)
