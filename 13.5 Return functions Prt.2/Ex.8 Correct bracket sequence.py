# объявление функции
def is_correct_bracket(text):
    text, count = list(text), 0
    if text[0] == ')' or text[-1] == '(':
        return False
    for i in text:
        if i == '(':
            count+=1
        if i == ')':
            count-=1
        if count == -1:
            return False
        #print(count)
    if count == 0:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
#Делать через счётчик