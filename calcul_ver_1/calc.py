
from tkinter import *
from tkinter import ttk
from decimal import *


root = Tk()
root.title("calcul_ver_2")

buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4')
           )

activeStr = ''
stack = []

def calcul_ver_1():
    global stack
    global label
    result = 0
    operand2 = Decimal(stack.pop())
    operation = stack.pop()
    operand1 = Decimal(stack.pop())
#    x = int(input("Введите первое число "))
#    y = int(input("Введите второе число "))
#    z = input("Введите операцию(+, *, -, /, возведение в степень ** ) ")

    if operation == '+':
        result = opera + y
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
    label.configure(text=str(result))
    print(result)


calcul_ver_1()


a = 2
b = 3
c = a % b


mainframe = ttk.Frame(root, padding="8 8 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

number = StringVar()
number_entry = ttk.Entry(mainframe, width=7, textvariable=number)
number_entry.grid(column=2, row=1, sticky=(W))

numbers = StringVar

