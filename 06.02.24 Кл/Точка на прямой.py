def line(s, t):
    x, y = map(int, t.split(':'))
    k, b = s.split('x')
    k = int(k)
    b = int(b)
    if y == k * x + b:
        print(True)
    else:
        print(False)


result = line("1x+6", "1;7")
print(result)
