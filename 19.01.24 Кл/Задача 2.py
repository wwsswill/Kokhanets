a, b = map(int, input('Введите два целых числа:\n').split())
product = 0
a1,b1 =a,b
if (a >= 0 and b >= 0) or (a < 0 and b < 0):
    a = abs(a)
    b = abs(b)
    while b > 0:
        product += a
        b -= 1
else:
    a = abs(a)
    b = abs(b)
    while b > 0:
        product -= a
        b -= 1
print(f"{a1} * {b1} = {product}")
