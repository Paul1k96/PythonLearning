# объявление функции
def is_palindrome(text):
    format = list(text.lower())
    k = 0
    while k!=len(format):
        if format[k] in ',.!?- ':
            del format[k]
            k = 0
        k+=1
    format = ''.join(format)
    return format == format[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))