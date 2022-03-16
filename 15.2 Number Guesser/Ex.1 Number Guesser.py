def number_guesser(guess):
    count = 0
    from random import randint
    n = randint(1, 100)
    count = 1
    guess = int(guess)
    while guess != n:
        if guess > n:
            print('Слишком много, попробуйте ещё раз!')
            guess = input()
            count += 1
        elif guess < n:
            print('Слишком мало, попробуйте ещё раз!')
            guess = input()
            count += 1
        if is_valid(guess) == True:
            guess = int(guess)
        else:
            while is_valid(guess) != True:
                guess = input('А может быть все-таки введем целое число от 1 до 100?')
            guess = int(guess)
    print('Число попыток:', count)
    return 'Вы угадали, поздравляем!'

def is_valid(n):
    if n.isdigit() == False:
        return False
    return int(guess) in range(1,101)

again = 'да'
guess = input('Это числовая угадайка в диапазоне от 1 до 100. Как думаете, какое число сейчас у меня в памяти? ')
while guess != 'нет':
    if is_valid(guess) == True:

        while again == 'да':
            print(number_guesser(guess))

            while again != 'да' or again != 'нет':
                again = input('Хотите ещё раз попробовать? Ответ "да" или "нет: "').lower()
                if again == 'нет':
                    break

            if again == 'нет':
                break
    else:
        guess = input('Неверное значение. Введите число от 1 до 100, либо введите "нет", если хотите выйти.').lower()
    if again == 'нет':
        break
print('Спасибо за игру!')


