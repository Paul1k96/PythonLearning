def get_word():
    from random import randrange
    word_list = ['ЧЕЛОВЕК', 'ЖИВОТНОЕ', 'КОМПЬЮТЕР', 'КАБЕЛЬ', 'ЭТАНОЛ', 'АЛЬБАТРОС', 'КОЛЛАЙДЕР']
    n = word_list[randrange(len(word_list))]
    return n

def check_cycle(a, b, c):
    a = list(a)
    for i in range(len(a)):
        if b == c[i]:
            a[i] = b
    a = ''.join(a)
    return a

def display_hangman(tries):
    stages = [ # финальное состояние: голова, торс, обе руки, обе ноги
               '''
                  --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
               ''',
               # голова, торс, обе руки, одна нога
               '''
                  --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
               ''',
               # голова, торс, обе руки
               '''
                  --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     
                   -
               ''',
               # голова, торс, одна рука
               '''
                  --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |      
                   -
               ''',
               # голова, торс
               '''
                  --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
               ''',
               # голова
               '''
                  --------
                   |      |
                   |      O
                   |      
                   |      
                   |     
                   -
               ''',
               # начальное состояние
               '''
                  --------
                   |      |
                   |      
                   |     
                   |      
                   |      
                   -
               '''
          ]
    return stages[tries]

def yes_no():
    print('Хотите ещё раз сыграть? "Да" или "Нет":')
    while True:
        a = input().lower()
        if a == 'нет' or a == 'да':
            return a
        else:
            print('Не понимаю. Введите пожалуйста "Да" или "Нет": ')

def play(word, hide_word, tries):
    while True:
        if hide_word == word:
            print('Вы угадали слово!')
            y_n = yes_no()
            if y_n == 'нет':
                return 'нет'
            else:
                break

        try_guess = input().upper()
        if try_guess in hide_word:
            print('Эта буква уже есть в списке! Попробуй ещё раз.')
            continue
        if try_guess in word and try_guess not in hide_word:
            hide_word = check_cycle(hide_word, try_guess, word)
            print('Правильно! Оставшееся слово:', hide_word)
        else:
            tries -= 1
            print('Не верно! Оставшееся слово:', hide_word)
            print(display_hangman(tries))
            if tries < 1:
                print('Загаданное слово:', word)
                y_n = yes_no()
                if y_n == 'нет':
                    return 'нет'
                else:
                    break



print('Добро пожаловать в игру "Виселица". В данной игре нужно угадывать буквы, из которого состоит слово. Не угадываешь - теряешь попытку. Всего попыток 6.')


while True:
    tries = 6
    word = get_word()
    print(word)
    hide_word = ''.join(list(word[0]) + ['_' for i in range(1, len(word) - 1)] + list(word[-1]))
    print('Начальная позиция виселицы:', display_hangman(tries), sep='\n')
    print('Угадаешь остальные буквы слова?')
    ansr = play(word, hide_word, tries)
    if ansr == 'нет':
        break

print('Спасибо за игру!')


