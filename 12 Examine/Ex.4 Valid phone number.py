cell_numb, flag1, flag2 = list(input()), False, True
count = cell_numb.count('-')
cell_numb = ''.join(cell_numb).split('-')

if count == 2 or count == 3:
    if cell_numb[0] == '7' and len(cell_numb[1]) == 3 and len(cell_numb[2]) == 3 and len(cell_numb[3]) == 4:
        flag1 = True
    elif len(cell_numb[0]) == 3 and len(cell_numb[1]) == 3 and len(cell_numb[2]) == 4:
        flag1 = True

if flag1 == True:
    for i in cell_numb:
        for j in range(len(i)):
            if i[j] not in '0123456789':
                flag2 = False
                break

if flag2 == True and flag1 == True:
    print('YES')
else:
    print('NO')
