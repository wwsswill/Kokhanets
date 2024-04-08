def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum


def ads(num1, num2):
    sum1 = sum_of_digits(num1)
    sum2 = sum_of_digits(num2)

    if sum1 > sum2:
        return f"Сумма цифр числа {num1} больше, чем у числа {num2}."
    elif sum1 < sum2:
        return f"Сумма цифр числа {num2} больше, чем у числа {num1}."
    else:
        return f"Сумма цифр чисел {num1} и {num2} равна."


number1 = 12345
number2 = 12345
result = ads(number1, number2)
print(result)
