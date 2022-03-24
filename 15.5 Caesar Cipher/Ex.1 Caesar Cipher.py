def caesar_cipher(lang, step, text):
    main_list = list(text)
    ru_list = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    en_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if lang == 'английский':
        main_list = lng(main_list, step, en_list)
    if lang == 'русский':
        main_list = lng(main_list, step, ru_list)
    return ''.join(main_list)


def lng(main_list, step, lang):
    alpha = len(lang)
    for i in range(len(main_list)):
        for k in range(alpha):
            if main_list[i] == lang[k] or main_list[i] == lang[k].lower():
                numb = k
        if numb-step < 0 and :
            main_list[i] = lang[numb - step + alpha]
        if numb-step>=0:
            main_list[i] = lang[numb - step]
    return main_list




print('Шифрование или дешифрование? ')
code_decode = input()
print('Алфавит русский или английский? ')
lang = input()
if code_decode == 'шифрование':
    print('Какой шаг сдвига(число, цифра)? ')
    step = int(input())
text = input('Введите текст: ')
print(caesar_cipher(lang,step,text))