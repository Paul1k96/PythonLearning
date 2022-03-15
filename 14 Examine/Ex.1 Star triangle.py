# объявление функции
def draw_triangle():
    star, s, count = '*', ' ', 8
    for i in range(8):
        count-=1
        print(s*count, star, sep='')
        tmp = star
        star = '*'
        star += tmp + star

# основная программа
draw_triangle()  # вызов функции