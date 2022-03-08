E = input().split()
for i in range(len(E)):
    E[i] = int(E[i])
print(*E, sep='+', end='')
print('=', sum(E), sep='')