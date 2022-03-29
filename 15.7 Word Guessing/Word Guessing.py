def get_word():
    from random import randint
    word_list = ['ЧЕЛОВЕК', 'ЖИВОТНОЕ', 'КОМПЬЮТЕР', 'КАБЕЛЬ', 'ЭТАНОЛ', 'АЛЬБАТРОС']
    n = randint(len(word_list))
    return n

def check_cycle(a, b):
    for i in range(len(a)):
        if b == a[i]:
            a[i] = b
    return a[i]

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
                   |     / 
                   -
               ''',
               # голова, торс
               '''
                  --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     / 
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


tries = 6
print('Добро пожаловать в игру "Виселица". В данной игре нужно угадывать буквы, из которого состоит слово. Не угадываешь - теряешь попытку. Всего попыток 6.')
print('Начальная позиция виселицы:', display_hangman(tries), sep='\n')
print('Первая и последняя буквы даны. Угадаешь остальные?')
word = get_word()
hide_word = list(word[0]) + ['_' for i in range(1, len(word)-1)] + list(word[-1])
print(''.join(hide_word))
while True:
    try_guess = input()
    if try_guess in word:
        hide_word = check_cycle(hide_word, try_guess)
        print('Правильно! Оставшиеся буквы:', hide_word)
    else:
        tries-=1
        print('Не верно!')
        print(display_hangman(tries))
        if tries < 0:
            print('Вы проиграли!')
            print('Хотите ещё раз сыграть? "Да" или "Нет":')
            yes_no = input()

