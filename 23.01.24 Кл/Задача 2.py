armstrong_number = []
for num in range(100, 1000):
    digit_sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        digit_sum += digit ** 3
        temp //= 10
    if num == digit_sum:
        armstrong_number.append(num)
print(armstrong_number)