from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Calculator(Frame):

    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.frame = self
        self.create_widget()

    def calc(self, key):
        global memory

        if key == '=':
            try:
                res = eval(self.calc_ent.get())
                self.calc_ent.insert(END, '=' + str(res))
            except:
                self.calc_ent.insert(END, 'Ошибка!!!')
                messagebox.showerror('Ошибка', 'Не корректные данные!')

        elif key == 'C':
            self.calc_ent.delete(0, END)

        elif key == '-/+':
            if '=' in self.calc_ent.get():
                self.calc_ent.delete(0, END)
            try:
                if self.calc_ent.get()[0] == '=':
                    self.calc_ent.delete(0)
                else:
                    self.calc_ent.insert(0, '-')
            except IndexError:
                pass

        else:
            self.calc_ent.insert(END, str(key))




    def create_widget(self):
        self.calc_ent = Entry(root, width=65)
        self.calc_ent.grid(row=0, column=0, columnspan=5)

        self.btns = [
            '7', '8', '9', '/', '%',
            '4', '5', '6', '*', '√',
            '1', '2', '3', '-', '-/+',
            '0', '.', 'C', '+', '=']

        r = 1
        c = 0

        for i in self.btns:
            self.btns = ttk.Button(root)
            self.btns['text'] = i
            self.btns['command'] = lambda x = i: self.calc(x)
            self.btns.grid(row=r, column=c)
            c += 1
            if c > 4:
                c = 0
                r += 1

root = Tk()
root.title('Калькулятор')
root.geometry('400x200')

calculator = Calculator(root)

root.mainloop()