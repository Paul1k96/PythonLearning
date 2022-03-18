def answer():
    from random import randrange
    pos = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом']
    dbt = ['Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да']
    ntrl = ['Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять']
    neg = ['Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
    all_answer = [pos, dbt, ntrl, neg]
    shr = randrange(len(all_answer))
    all_answer = all_answer[shr]
    shr = randrange(len(all_answer))
    all_answer = all_answer[shr]
    return all_answer

def wrong(a):
    while True:
        a = input('Не понимаю. Введите пожалуйста "Да" или "Нет": ').lower()
        if a == 'да' or a == 'нет':
            return a
        else:
            continue

def qstn():
    input(f'{name} на какой вопрос ты хочешь получить ответ? Вопрос: ')
    print(answer())

name = input('Введите пожалуйста имя пользователя: ')
print(f'Привет {name}, я магический шар и я знаю ответ на любой вопрос.')

nxt = 'да'
while True:
    if nxt == 'нет':
        break
    while True:
        if nxt == 'да':
            qstn()
            break
        else:
            break
    nxt = input('Хотел бы задать ещё один вопрос или пока всё? Ответ "Да" или "Нет": ').lower()
    if nxt == 'да':
        continue
    elif nxt == 'нет':
        break
    else:
        nxt = wrong(nxt)

print(f'{name} спасибо за визит! Надеюсь, что мы ещё поиграем :)')