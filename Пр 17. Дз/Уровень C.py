def f_long_word(input_string):
    words = input_string.split()
    long_word = max(words, key=len)
    return long_word, len(long_word)


input_string = input("Введите строку:\n")
long_word, lenght = f_long_word(input_string)
print(f"Самое длинное слово: {long_word}, длина {lenght}")
