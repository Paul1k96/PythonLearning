# объявление функции
def convert_to_python_case(text):
    text = list(text)
    for i in range(1, len(text)):
        if text[i] == text[i].upper():
            text[i] = text[i].lower()
            text.insert(i, '_')
            i=0
    text = ''.join(text)
    return text.lower()


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))