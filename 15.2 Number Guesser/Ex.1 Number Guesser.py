def number_guesser(a, b):
    count = 0
    from random import randint
    n = randint(1, b)
    count = 1
    a = int(a)
    while a != n:
        if a > n:
            print('Слишком много, попробуйте ещё раз!')
            a = input()
            count += 1
        elif a < n:
            print('Слишком мало, попробуйте ещё раз!')
            a = input()
            count += 1
        if is_valid(a, b) == True:
            a = int(a)
        else:
            while is_valid(a, b) != True:
                print('А может быть все-таки введем целое число от 1 до', b, '? :')
                a = input()
            a = int(a)
    print('Число попыток:', count)
    return 'Вы угадали, поздравляем!'

def is_valid(g, e):
    if str(g).isdigit() == False:
        return False
    return int(g) in range(1, int(e)+1)

numb = input('Добро пожаловать! Это числовая угадайка. Задайте максимальный диапазон целым числом начиная от 1 до: ')
while is_valid(numb, numb) != True:
    if is_valid(numb, numb) == True:
        break
    else:
        numb = input('Неверное значение. Введите целое число начиная от 1: ')

print('Задан числовой диапазон от 1 до', numb)
guess = input('Как думаете, какое число сейчас у меня в памяти? Ответ: ')
again = 'да'
while guess != 'нет':
    if is_valid(guess, numb) == True:
        guess = int(guess)
        numb = int(numb)

        while again == 'да':
            print(number_guesser(guess, numb))

            while True:
                again = input('Хотите ещё раз попробовать? Ответ "да" или "нет: "').lower()
                if again == 'нет':
                    break
                elif again == 'да':
                    break

            if again == 'нет':
                break
    else:
        guess = input('Неверное значение. Введите число от 1 до 100, либо введите "нет", если хотите выйти: ').lower()
    if again == 'нет':
        break
print('Спасибо за игру!')