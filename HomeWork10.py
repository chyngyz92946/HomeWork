from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('Калькулятор')
root.geometry('392x150')

def calc(key):
    global memory
    if key == '=':
        str_1 = '1234567890/%*√-+.'
        if entry_1.get()[0] not in str_1:
            entry_1.insert(END, 'Ошибка!!!')
            messagebox.showerror('Ошибка', 'Не корректные данные!')
        try:
            res = eval(entry_1.get())
            entry_1.insert(END, '=' + str(res))
        except:
            entry_1.insert(END, 'Ошибка!!!')
            messagebox.showerror('Ошибка', 'Не корректные данные!')

    elif key == 'C':
        entry_1.delete(0, END)

    elif key == '-/+':
        if '=' in entry_1.get():
            entry_1.delete(0, END)
        try:
            if entry_1.get()[0] == '=':
                entry_1.delete(0)
            else:
                entry_1.insert(0, '-')
        except IndexError:
            pass

    else:
        if '=' in entry_1.get():
            entry_1.delete(0, END)
        entry_1.insert(END, key)

btns = [
    '7', '8', '9', '/', '%',
    '4', '5', '6', '*', '√',
    '1', '2', '3', '-', '-/+',
    '0', '.', 'C', '+', '='
]
r = 1
c = 0
for i in btns:
    rel = ''
    command = lambda x = i: calc(x)
    ttk.Button(root, text=i, command=command).grid(row=r, column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1

entry_1 = Entry(root, width=65)
entry_1.grid(row=0, column=0, columnspan=5)


root.mainloop()