# объявление функции
def number_to_words(num):
    numb = list(str(num))
    for i in range(len(numb)):
        numb[i] = int(numb[i])
    list1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    list2 = ['десять','одиннадцать','двенадцать','тринадцать','четырнадцать','пятнадцать','шестнадцать','семнадцать','восемнадцать','девятнадцать']
    list3 = ['двадцать','тридцать','сорок','пятьдесят','шестьдесят','семьдесят','восемьдесят','девяносто']
    if len(numb)==1:
        return list1[num-1]
    if len(numb)==2 and numb[0]==1:
        return list2[numb[1]]
    if len(numb)==2 and numb[0]!=1:
        if numb[1]==0:
            return list3[numb[0]-2]
        else:
            return list3[numb[0]-2]+' '+list1[numb[1]-1]


# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))