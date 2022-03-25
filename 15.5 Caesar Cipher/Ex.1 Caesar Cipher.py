def caesar_cipher(c, lang, step, text):
    main_list = list(text)
    ru_list = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    en_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if c == 'b':
        step*=-1
    if lang == 'en':
        main_list = lng(main_list, step, en_list)
    if lang == 'ru':
        main_list = lng(main_list, step, ru_list)
    return ''.join(main_list)

def lng(main_list, step, lang):
    alpha = len(lang)
    if step<0:
        step*=-1
        for i in range(len(main_list)):
            if main_list[i].isalpha() != True:
                continue

            for k in range(alpha):
                if main_list[i] == lang[k] or main_list[i] == lang[k].lower():
                    numb = k

            if numb-step < 0 and main_list[i] == main_list[i].lower() : # Отрицательный шаг
                main_list[i] = lang[numb - step + alpha].lower()
            if numb-step>=0 and main_list[i] == main_list[i].lower():
                main_list[i] = lang[numb - step].lower()
            if numb-step < 0 and main_list[i] == main_list[i].upper() :
                main_list[i] = lang[numb - step + alpha]
            if numb-step>=0 and main_list[i] == main_list[i].upper():
                main_list[i] = lang[numb - step]

    else:
        for i in range(len(main_list)):
            if main_list[i].isalpha() != True:
                continue

            for k in range(alpha):
                if main_list[i] == lang[k] or main_list[i] == lang[k].lower():
                    numb = k

            if numb+step >= alpha and main_list[i] == main_list[i].lower() :
                main_list[i] = lang[numb + step - alpha].lower()
            if numb+step < alpha and main_list[i] == main_list[i].lower():
                main_list[i] = lang[numb + step].lower()
            if numb+step >= alpha and main_list[i] == main_list[i].upper() : # Положительный шаг
                main_list[i] = lang[numb + step - alpha].upper()
            if numb+step < alpha and main_list[i] == main_list[i].upper():
                main_list[i] = lang[numb + step].upper()

    return main_list

def dig():
    while True:
        a = input()
        if a.isdigit() == True:
            a = int(a)
            return a
        else:
            print('Не понимаю. Введите пожалуйста число.')
            continue

def cd():
    while True:
        a = input()
        if a == 'a' or a == 'A':
            return 'a'
        elif a == 'b' or a == 'B':
            return 'b'
        else:
            print('Ответ "a" или "b": ')
            continue

def lng():
    while True:
        a = input()
        if a == 'ru' or a == 'RU':
            return 'ru'
        elif a == 'en' or a == 'EN':
            return 'en'
        else:
            print('Ответ "ru" или "en": ')
            continue

print('Шифрование(a) или дешифрование(b)? ')
code_decode = cd()
print('Алфавит русский или английский (ru или eng)? ')
lang = lng()
if code_decode =='a':
    print('Какой шаг сдвига(число, цифра)? ')
    step = dig()
else:
    print('Какой шаг был при шифровании? ')
    step = dig()
text = input('Введите текст: ')
print(caesar_cipher(code_decode, lang, step, text))