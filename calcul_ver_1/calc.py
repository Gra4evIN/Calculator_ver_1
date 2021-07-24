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


def calcul_ver_2():
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
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
        result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2
    # elif z == '/' and y != 0:
    #   result = x / y
    # if y == 0:
    #   result = (print('Деление на ноль невозможно'))
    label.configure(text=str(result))
    # print(result)


def click(text):
    global activeStr
    global stack
    if text == 'CE':
        stack.clear()
        activeStr = ''
        label.configure(text='0')
    elif '0' <= text <= '9':
        activeStr += text
        label.configure(text=activeStr)
    elif text == '.':
        if activeStr.find('.') == -1:
            activeStr += text
            label.configure(text=activeStr)
    else:
        if len(stack) >= 2:
            stack.append(label['text'])
            calcul_ver_2()
            stack.clear()
            stack.append(label['text'])
            activeStr = ''
            if text != '=':
                stack.append(text)

        else:
            if text != '=':
                stack.append(label['text'])
                stack.append(text)
                activeStr = ''
                label.configure(text='0')

label = Label(root, text='0', width=35)
label.grid(row = 0, column=0, columnspan=4, sticky="nsew")

button = Button(root, text = 'CE', command = lambda text='CE': click(text))
button.grid(row=1, column=3, sticky='nsew')
for row in range(4):
    for col in range(4):
        button = Button(root, text=buttons[row][col],
                        command=lambda row=row, col=col: click(buttons[row][col]))
        button.grid(row=row + 2, column=col, sticky="nsew")

rott.grid_rowconfigure(6, weight=1)
root.columnconfigure(4, weight=1)

root.mainloop()



calcul_ver_2()

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
