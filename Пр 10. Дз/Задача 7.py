def prime_factors(n, divisor=2):
    if n <= 1:
        return

    if n % divisor == 0:
        if n != divisor:
            print(divisor, end="*")
            prime_factors(n // divisor, divisor)
        else:
            print(divisor)
    else:
        prime_factors(n, divisor + 1)


num = int(input("Введите натуральное число: "))
print(f"{num} = ", end="")
prime_factors(num)
