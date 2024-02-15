def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


num1 = 7006652
num2 = 112307574

result = gcd(num1, num2)
print(f"НОД({num1}, {num2}) = {result}.")
