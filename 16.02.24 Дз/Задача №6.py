def reverse_number(number):
    reversed_number = int(str(number)[::-1])
    return reversed_number


number = 2621

reversed_number = reverse_number(number)
print(f"После переворота: {reversed_number}.")
