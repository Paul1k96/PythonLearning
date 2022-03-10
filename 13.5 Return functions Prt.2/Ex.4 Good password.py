# объявление функции
def is_password_good(password):
    list_for_check = list(password)
    points = 0
    if len(list_for_check)>=8:
        points+=1
    for i in list_for_check:
        if i == i.upper() and not i in '0123456789':
            points+=1
            break
    for i in list_for_check:
        if i == i.lower() and not i in '0123456789' :
            points+=1
            break
    for i in list_for_check:
        if i in '0123456789':
            points+=1
            break
    if points == 4:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))