import random


def ch_dup(array):
    seen = {}
    dup = set()

    for num in array:
        if num in seen:
            dup.add(num)
        seen[num] = True

    return dup


array = [random.randint(0, 5) for _ in range(5)]

dup = ch_dup(array)
print("Массив:")
print(' '.join(map(str, array)))

if dup:
    print("Есть:", ', '.join(map(str, dup)))
else:
    print("Нет")