#import math
def calcul_ver_1(x, y, z):

    global result
    x = int(input("Введите первое число "))
    y = int(input("Введите второе число "))
    z = input("Введите операцию(+, *, -, /, возведение в степень ** ) ")


    if z == '+':
        result = x + y
    elif z == '*':
        result = x * y
    elif z == '-':
        result = x - y
    elif z == '**':
        result = x ** y
    elif z == '/' and y != 0:
        result = x / y
    if y == 0:
        result = (print('Деление на ноль невозможно'))

    print(result)


#calcul_ver_1(1, 2, '*')


#a = 2
#b = 3
#c = a % b
