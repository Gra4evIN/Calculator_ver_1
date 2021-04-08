import math

a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
c = input("Введите операцию(+, *, -, /, возведение в степень ** ) ")


if c == '+':
    result = a + b
elif c == '*':
    result = a * b
elif c == '-':
    result = a - b
elif c == '/' and b != 0:
    result = a / b
if b == 0:
    print('Деление на ноль невозможно')
elif c == '**':
    result = a ** b

print(result)










