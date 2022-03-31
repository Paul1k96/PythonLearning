def get_word():
    from random import randrange
    cat1 = ['Животный мир','ЧЕЛОВЕК', 'ЖИВОТНОЕ', 'ЖИРАФ', 'КОАЛА', 'ЛЕОПАРД', 'АЛЬБАТРОС', 'КАМБАЛА']
    cat2 = ['Технологии','ПРОЦЕССОР', 'МОНИТОР', 'КОМПЬЮТЕР', 'КАБЕЛЬ', 'РОУТЕР', 'СМАРТФОН', 'КОЛЛАЙДЕР']
    cat3 = ['Химия','КРЕМНИЙ', 'РЕЗИНА', 'БЕНЗИН', 'МЕТАНОЛ', 'ЭТАНОЛ', 'УРАН', 'ПЛАСТИК']
    cat4 = ['Растения','РОМАШКА', 'ФИАЛКА', 'БАОБАБ', 'БЕРЁЗА', 'АЛОЭ', 'КЛЁН', 'ЧЕРЕШНЯ']

    while True:
        cat = input(f'Выберите категорию. {cat1[0]}(1), {cat2[0]}(2), {cat3[0]}(3), {cat4[0]}(4): ').upper()
        if cat == '1':
            word_list = cat1[1:]
            break
        elif cat == '2':
            word_list = cat2[1:]
            break
        elif cat == '3':
            word_list = cat3[1:]
            break
        elif cat == '4':
            word_list = cat4[1:]
            break
        else:
            print('Не понимаю.')
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
        if try_guess in hide_word[1:len(hide_word)-1]:
            print('Эта буква уже есть в списке! Попробуй ещё раз.')
            continue
        elif try_guess in word and try_guess not in hide_word[1:len(hide_word)-1]:
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


