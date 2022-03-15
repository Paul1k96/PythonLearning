# объявление функции
def get_month(language, number):
    ru_mnth = ['январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь']
    en_mnth = ['january','february','march','april','may','june','july','august','september','october','november','december']
    if language == 'ru':
        return ru_mnth[number-1]
    if language == 'en':
        return en_mnth[number - 1]

# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))