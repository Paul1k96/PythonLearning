# объявление функции
def draw_triangle(fill, base):
    for i in range(1, base//2+1):
        print(i*fill)
    for j in range(base//2+1, 0, -1):
        print(j*fill)
    pass

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)