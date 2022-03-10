# объявление функции
def get_next_prime(num):
    for i in range(num+1, 10000):
        count = 0
        for j in range(1, i+1):
            if i%j == 0:
                count += 1
        if count == 2:
            return i

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))