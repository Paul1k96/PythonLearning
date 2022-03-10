# объявление функции
def is_prime(num):
    count = 0
    for i in range(1, num+1):
        if num%i==0:
            count+=1
    if count == 2:
        prime = True
    else:
        prime = False
    return prime

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))