a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))

sum = 0
for num in range(a, b + 1):
    sum += num
print("Сумма всех целых чисел от", a, "да", b, ":", sum)
