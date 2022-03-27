#блок для подготовки к зашифровке текста
def caesar_cipher(text):
    main_list = list(text) # вводимый текст, раздробленный в массив
    cnt_list = count_list(main_list) # лист с кол-вом букв в каждом слове
    en_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = 0 # счётчик-флаг для прерывания цикла проверки на букву(0 или 1)
    list_count = 0 # счётчик для переключения
    step = cnt_list[0] # первое число списка с кол-вом букв
    for i in range(len(main_list)):
        if main_list[i].isalpha() != True:
            if count > 0:
                continue

            count += 1
            list_count+=1
            if list_count == len(cnt_list):
                continue
            step = cnt_list[list_count]

        else:
            main_list[i] = lng(main_list[i], step, en_list)
            count = 0

    return ''.join(main_list)

#блок для зашифровки текста
def lng(main_list, step, lang):
    alpha = len(lang)
    for i in range(len(main_list)):

        for k in range(alpha):
            if main_list[i] == lang[k] or main_list[i] == lang[k].lower():
                numb = k

        if numb + step >= alpha and main_list[i] == main_list[i].lower():
            main_list = lang[numb + step - alpha].lower()
        if numb + step < alpha and main_list[i] == main_list[i].lower():
            main_list = lang[numb + step].lower()
        if numb + step >= alpha and main_list[i] == main_list[i].upper():
            main_list = lang[numb + step - alpha].upper()
        if numb + step < alpha and main_list[i] == main_list[i].upper():
            main_list = lang[numb + step].upper()

    return main_list

#создание списка чисел букв в каждом слове
def count_list(main_list):
    count_list = []
    count = 0
    for i in range(len(main_list)):
        if main_list[i].isalpha() == True:
            count += 1
        else:
            if count == 0:
                continue
            count_list += str(count)
            count = 0
    if count > 0:
        count_list += str(count)
    for i in range(len(count_list)): # перевод списка в int
        count_list[i] = int(count_list[i])
    return count_list

print(caesar_cipher(input()))