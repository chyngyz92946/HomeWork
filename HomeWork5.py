from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import *

def new_file(event=None):
    root.title('Безымянный.txt')
    txt.delete(0.0, END)

def open_file(event=None):
    of = askopenfilename()
    file = open(of, mode='r')
    txt.insert(END, file.read())
    file.close()

def save_file(event=None):
    sf = asksaveasfilename()
    final_text = txt.get(1.0, END)
    file = open(sf + '.txt', mode='w')
    file.write(final_text)
    file.close()

def save_as():
    sf = asksaveasfilename()
    final_text = txt.get(1.0, END)
    file = open(sf, mode='w')
    file.write(final_text)
    file.close()

def cut():
    txt.event_generate('<<Cut>>')

def copy():
    txt.event_generate('<<Copy>>')

def paste():
    txt.event_generate('<<Paste>>')

def select_all():
    txt.event_generate('<<SelectAll>>')

def clear():
    txt.event_generate('<<Clear>>')

def popup(event):
    pmenu.tk_popup(event.x_root, event.y_root)

def close():
    if askyesno('Выход', 'Вы хотите выйти?'):
        root.destroy()

root = Tk()
root.geometry('600x350')
root.title('Блокнот')

main_menu = Menu(root)
root.configure(menu=main_menu)

txt = Text(root, width=40, height=15, font=12)
txt.pack(expand=YES, fill=BOTH)
txt.bind('<Button-3>', popup)
txt.bind('<Control-n>', new_file)
txt.bind('<Control-o>', open_file)
txt.bind('<Control-s>', save_file)
txt.bind('<Control-a>', select_all)
txt.bind('<Delete>', clear)


first_item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Файл', menu=first_item)

first_item.add_command(label='Создать', accelerator='CTRL+N', command=new_file)
first_item.add_command(label='Открыть...', accelerator='CTRL+O', command=open_file)
first_item.add_command(label='Сохранить', accelerator='CTRL+S', command=save_file)
first_item.add_command(label='Сохранить как...', command=save_as)
first_item.add_separator()
first_item.add_command(label='Параметры страницы...')
first_item.add_command(label='Печать', accelerator='CTRL+P')
first_item.add_separator()
first_item.add_command(label='Выход', command=close)

second_item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Правка', menu=second_item)

second_item.add_command(label='Отменить', accelerator='CTRL+Z')
second_item.add_separator()
second_item.add_command(label='Вырезать', accelerator='CTRL+X', command=cut)
second_item.add_command(label='Копировать', accelerator='CTRL+C', command=copy)
second_item.add_command(label='Вставить', accelerator='CTRL+V', command=paste)
second_item.add_command(label='Удалить', accelerator='DEL', command=clear)
second_item.add_separator()
second_item.add_command(label='Найти...', accelerator='CTRL+F')
second_item.add_command(label='Найти далее', accelerator='F3')
second_item.add_command(label='Заменить...', accelerator='CTRL+H')
second_item.add_command(label='Перейти...', accelerator='CTRL+G')
second_item.add_separator()
second_item.add_command(label='Выделить всё', accelerator='CTRL+A', command=select_all)
second_item.add_command(label='Время и дата', accelerator='F5')

third_item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Формат', menu=third_item)

third_item.add_command(label='Перенос по словам')
third_item.add_command(label='Шрифт...')

fourth_item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Вид', menu=fourth_item)

fourth_item.add_command(label='Строка состояния')

fifth_item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Справка', menu=fifth_item)

fifth_item.add_command(label='Просмотреть справку')
fifth_item.add_separator()
fifth_item.add_command(label='О программе', command=lambda: showinfo('О программе', 'Домашнее задание блокнот'))

pmenu = Menu(txt, tearoff=0)
pmenu.add_command(label='Отменить')
pmenu.add_separator()
pmenu.add_command(label='Вырезать', command=cut)
pmenu.add_command(label='Копировать', command=copy)
pmenu.add_command(label='Вставить', command=paste)
pmenu.add_command(label='Удалить', command=clear)
pmenu.add_separator()
pmenu.add_command(label='Выделить всё', command=select_all)

root.protocol('WM_DELETE_WINDOW', close)

root.mainloop()