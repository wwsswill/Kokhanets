def countw(n):
    if n == 1:
        return 1
    else:
        abc = 0
        for i in range(1, n + 1):
            abc += countw(n - i)
        return abc 


n = int(input("Введите натуральное число:\n"))
print(f"Количество разложений: {countw}")
