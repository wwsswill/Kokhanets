import random
rost_ych = [random.randint(150, 190) for _ in range(30)]

rost_bolshe_170 = sum(1 for rost in rost_ych if rost > 170)
rost_menshe_170 = sum(1 for rost in rost_ych if rost < 170)
if rost_bolshe_170 >= 5:
    print("Количество учеников с ростом больше 170 см:", rost_bolshe_170)
    print("Можно сформировать баскетбольную команду!")
else:
    print("Количество учеников с ростом ниже 170 см:", rost_menshe_170)
    print("Нельзя сформировать команду")
