# объявление функции
def number_of_factors(num):
    count = 0
    for i in range(1, num+1):
        if num%i == 0:
            count+=1
    return count

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))