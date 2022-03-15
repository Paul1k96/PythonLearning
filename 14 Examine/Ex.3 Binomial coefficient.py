# объявление функции
def compute_binom(n, k):
    from math import factorial
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))