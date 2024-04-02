import random

mass_h = [random.randint(70, 140) for _ in range(25)]

p_h = []
o_h = []
for mass in mass_h:
    if mass > 100:
        p_h.append(mass)
    else:
        o_h.append(mass)

s_mass_p = sum(p_h) / len(p_h)
s_mass_o = sum(o_h) / len(o_h)

print("Средняя масса полных людей:", s_mass_p)
print("Средняя масс остальных людей:", s_mass_o)