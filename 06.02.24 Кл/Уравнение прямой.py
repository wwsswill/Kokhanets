def equation(a, b):
    x1, y1 = map(float, a.split(';'))
    x2, y2 = map(float, b.split(';'))

    if x1 == x2:
        c = x1
        print(f'{y2 - y1:.1f} {c:.1f}')
    elif y1 == y2:
        c = y1
        print(f'0.0 {c:.1f}')
    else:
        k = (y2 - y1) / (x2 - x1)
        b = y1 - k * x1
        print(f'{k:.1f} {b:.1f}')


a = input()
b = input()
equation(a, b)
