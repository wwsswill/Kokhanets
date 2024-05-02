def encode_string(s):
    if not s:
        return ""

    encoded = []
    current_char = s[0]
    count = 0
    for char in s:
        if char == current_char:
            count += 1
        else:
            encoded.append(current_char + str(count))
            current_char = char
            count = 1
    encoded.append(current_char + str(count))
    return ''.join(encoded)


input_string = input("Введите строку:\n")
encode_string = encode_string(input_string)
print("Закодированная строка:", encode_string)
