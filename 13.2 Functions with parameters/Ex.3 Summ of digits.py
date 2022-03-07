# объявление функции
def print_digit_sum(n):
    n = str(n)
    s.extend(n)
    for i in range(len(s)):
        s[i] = int(s[i])
    print(sum(s))

# считываем данные
n,s = int(input()), []

# вызываем функцию
print_digit_sum(n)