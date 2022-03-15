# объявление функции
def is_magic(date):
    date = date.split('.')
    y = date[2]
    for i in range(len(date)):
        date[i] = int(date[i])
    return date[0]*date[1] == int(y[2:])

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))