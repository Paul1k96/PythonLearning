def alpha():
    char = ''
    print('Включать в генератор числа? ')
    if qstn() == 'yes':
        char += '0123456789'

    print('Включать в генератор прописные буквы?')
    if qstn() == 'yes':
        char += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    print('Включать в генератор строчные буквы?')
    if qstn() == 'yes':
        char += ('ABCDEFGHIJKLMNOPQRSTUVWXYZ').lower()

    print('Включать в генератор символы?')
    if qstn() == 'yes':
        char += '!#$%&*+-=&@^_'

    print('Исключить из генератора неоднозначные символы (il1Lo0O)?')
    if qstn() == 'yes':
        char = list(char)
        for i in 'il1Lo0O':
            if i in char:
                char.remove(i)
        char = ''.join(char)
    return char

def password(count):
    from random import randrange
    char = alpha()
    if len(char) == 0:
        return print('Список генератора пуст.')
    result = []
    for i in range(count):
        pss = ''
        print('Введите длинну пароля:', end=' ')
        length = dig()
        for j in range(length):
            pss += char[randrange(len(char))]
        result += [pss]
    return result

def qstn():
    while True:
        a = input('Ответ "Yes" или "no": ')
        if a == 'yes':
            return 'yes'
        elif a == 'no':
            return 'no'
        else:
            continue

def dig():
    while True:
        a = input()
        if a.isdigit() == True:
            a = int(a)
            return a
        else:
            print('Не понимаю. Введите пожалуйста число.')
            continue

def wrong(a):
    while True:
        a = input('Не понимаю. Введите пожалуйста "Yes" или "No": ').lower()
        if a == 'yes' or a == 'no':
            return a
        else:
            continue

print('Введите количество паролей для генерации:', end= ' ')
count = dig()
print('Пароли:', *password(count), sep = '\n')