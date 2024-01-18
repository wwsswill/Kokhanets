N = int(input('Введите число N: '))
prev_num = 1
curr_num = 1
fib_sum = 1
while curr_num < N:
    fib_sum += curr_num

    next_num = prev_num + curr_num
    prev_num = curr_num
    curr_num = next_num
print('Сумама', fib_sum)
