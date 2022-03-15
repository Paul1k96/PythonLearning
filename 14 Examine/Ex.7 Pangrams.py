# объявление функции
def is_pangram(text):
    alp = [chr(97+i) for i in range(26)]
    text, list1 = list(text.lower()), []
    for i in text:
        if i in list1:
            continue
        if i == ' ':
            continue
        list1+=i
    list1.sort()
    return list1 == alp

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))