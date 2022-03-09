# объявление функции
def get_factors(num):
    count = []
    for i in range(1, num+1):
        if num%i == 0:
            count.append(i)
    return count

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))