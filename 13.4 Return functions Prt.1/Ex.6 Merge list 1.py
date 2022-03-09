# объявление функции
def merge(list1, list2):
    list1+=list2
    for i in range(len(list1)):
        c = i
        for j in range(i+1, len(list1)):
            if list1[j] < list1[c]:
                c = j
        list1[c], list1[i] = list1[i], list1[c]
    return list1

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))