# объявление функции
def is_one_away(word1, word2):
    list1, list2 = list(word1), list(word2)
    l1, l2 = len(list1), len(list2)
    points = 0
    if l1 == l2:
        for i in range(l1):
            if list1[i] != list2[i] and points<=1:
                points+=1
            if points>1:
                return False
        if points == 0:
            return False
        else:
            return True
    else:
        return False

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))