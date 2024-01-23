n = int(input("Введите значение n:"))
count = 0
for num in range(100, 1000):
    digit_sum = sum(int(digit) for digit in str(num))
    if digit_sum == n:
        count += 1
print("Количество трехзначных натуральных чисел с суммой цифр, равной", n, ":", count)