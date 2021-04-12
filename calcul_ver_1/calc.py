import math

x = int(input("Введите первое число "))
y = int(input("Введите второе число "))
z = input("Введите операцию(+, *, -, /, возведение в степень ** ) ")


if z == '+':
    result = x + y
elif z == '*':
    result = x * y
elif z == '-':
    result = x - y
elif z == '/' and y != 0:
    result = x / y
if y == 0:
    print('Деление на ноль невозможно')
elif z == '**':
    result = x ** y

print(result)










