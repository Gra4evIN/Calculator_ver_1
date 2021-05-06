# import math
from unittest import result


def calcul_ver_1():
    while True:
        print("Выберите операцию:\n"
              "Сложение: +\n"
              "Умножение: *\n"
              "Вычитание: -\n"
              "Деление: /\n"
              "Возведение в степень: **\n"
              "Закрыть программу: q\n")
        operation = input("Ввод: ")
        if operation == 'q':
            print("Конец программы")
            break

        if operation in ('+', '*', '-', '/', '**'):
            x = float(input("x= "))
            y = float(input("y = "))

            if operation == '+':
                result = (x, y, int(x + y))
            elif operation == '*':
                result = (x, y, int(x * y))
            elif operation == '-':
                result = (x, y, int(x - y))
            elif operation == '**':
                result = (x, y, int(x ** y))
            elif operation == '/':
                if y != 0:
                    result = (x, y, int(x / y))
                else:
                    print('Деление на ноль невозможно')
        print(result)




print(calcul_ver_1())

# a = 2
# b = 3
# c = a % b
