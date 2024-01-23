def is_automoprophic(n):
    square = n ** 2
    return str(square)[-len(str(n)):] == str(n)


def automorphic_numbers(n):
    for i in range(1, n + 1):
        if is_automoprophic(i):
            print(f"{i} * {i} = {i ** 2}")


N = int(input("Введите N:"))
automorphic_numbers(N)