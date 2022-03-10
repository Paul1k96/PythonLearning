# объявление функции
def is_valid_password(password):
    password = list(password)
#------------------------------------------------------------------
    count = password.count(':')
    if count!=2:
        return False
#-------------------------------------------------------------------
    a = ''.join(separator(password))
    if a != a[::-1]:
        return False
#-------------------------------------------------------------------
    b = int(''.join(separator(password[password.index(':')+1:])))
    count = 0
    if b == 1:
        return False
    for i in range(2, b):
        if b%i == 0:
            return False
#--------------------------------------------------------------------
    c = int(''.join(separator(password[-1])))
    if c%2!=0:
        return False
#--------------------------------------------------------------------
    return True

def separator(part):
    result = []
    for i in range(len(part)):
        if part[i] == ':':
            break
        result+=part[i]
    return result

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))