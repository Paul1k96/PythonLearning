def caesar_cipher(text):
    main_list = list(text)
    count_list = count_list(main_list)
    en_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    second_list = ''.join([i for i in main_list if i not in '!&.,"?']).split()
    #second_list = ''.join([i for i in main_list]).split()
    for i in range(len(second_list)):

    return ''.join(main_list)

def lng(main_list, step, lang):
    alpha = len(lang)
    for i in range(len(main_list)):
        if main_list[i].isalpha() != True:
            continue

        for k in range(alpha):
            if main_list[i] == lang[k] or main_list[i] == lang[k].lower():
                numb = k

        if numb + step >= alpha and main_list[i] == main_list[i].lower():
            main_list[i] = lang[numb + step - alpha].lower()
        if numb + step < alpha and main_list[i] == main_list[i].lower():
            main_list[i] = lang[numb + step].lower()
        if numb + step >= alpha and main_list[i] == main_list[i].upper():  # Положительный шаг
            main_list[i] = lang[numb + step - alpha].upper()
        if numb + step < alpha and main_list[i] == main_list[i].upper():
            main_list[i] = lang[numb + step].upper()

    return main_list

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
    return count_list

text = input()

print(caesar_cipher(text))