def is_perfect_number(number):
    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i

    if divisors_sum == number:
        return True
    else:
        return False


num = int(input("Введите натуральное число: "))
if is_perfect_number(num):
    print(f"Число {num} совершенное.")
else:
    print(f"Число {num} не совершенное.")
