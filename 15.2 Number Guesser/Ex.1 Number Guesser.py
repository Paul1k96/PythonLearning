def number_guesser(guess):
    count = 0
    from random import randint
    n = randint(1, 100)
    count = 1
    while guess != n:
        if guess > n:
            print('Слишком много, попробуйте ещё раз!')
            guess = int(input())
            count += 1
        if guess < n:
            print('Слишком мало, попробуйте ещё раз!')
            guess = int(input())
            count += 1
    print('Число попыток:', count)
    return 'Вы угадали, поздравляем!'

again = 'да'
while again == 'да':
    guess = int(input('Это числовая угадайка. Как думаете, какое число сейчас у меня в памяти? '))
    print(number_guesser(guess))
    again = input('Хотите ещё раз попробовать? Ответ "да" или "нет: "')



