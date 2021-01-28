import tkinter as tk
from tkinter import *
import random
import string
from tkinter import messagebox as mb


def get_password():
    if choice.get() == 1:
        return "".join(random.sample(upper, value.get()))

    elif choice.get() == 2:
        return "".join(random.sample(lower, value.get()))

    elif choice.get() == 3:
        return "".join(random.sample(symbols, value.get()))

    elif choice.get() == 4:
        return "".join(random.sample(numbers, value.get()))


def generate_password():
    password_field.config(text=get_password())


def get_value_length(val=1):
    print(int(val))
    return int(val)


def selection():
    choice.get()


window = tk.Tk()

window.geometry(f'480x450+100+200')
window.resizable(False, False)
window['bg'] = '#5F4843'
window.title('Password generator')
main_menu = Menu(window)
window.config(menu=main_menu)

filemenu = Menu(main_menu, tearoff=0)
filemenu.add_command(label='Открыть. . .')
filemenu.add_command(label='Новый')
filemenu.add_command(label='Сохранить. . .')
filemenu.add_command(label='Выход')

helpmenu = Menu(main_menu, tearoff=0)
helpmenu.add_command(label='Помощь')
helpmenu.add_command(label='О программе')

main_menu.add_cascade(label='Файл',
                      menu=filemenu)
main_menu.add_cascade(label='Справка',
                      menu=helpmenu)

choice = IntVar()
value = IntVar()

choose_length = Label(window,
                      text='Choose length of password:',
                      fg='black', bg='#5F4843', justify=LEFT,
                      font="Arial 11", relief=RIDGE
                      )
choose_length.grid(row=2, column=1, padx=20, pady=20, sticky=W)

scale_length = Spinbox(window,
                       fg='black',
                       from_=8,
                       to_=24,
                       textvariable=value)
scale_length.grid(row=2, column=2, pady=10)

configuration_for_pass = Label(window,
                               text='Choose symbols of your password:',
                               fg='black', bg='#5F4843', justify=LEFT,
                               font="Arial 11", relief=RIDGE
                               )
configuration_for_pass.grid(row=3, column=1, padx=20, pady=40, sticky=W)

with_uppers = Radiobutton(text='Upper case',
                          bg='#5F4843', fg='black',
                          variable=choice,
                          command=selection,
                          value=1)

with_uppers.grid(sticky=W, row=4, column=2, padx=40)

with_lowers = Radiobutton(text='Lower case',
                          bg='#5F4843',
                          fg='black',
                          variable=choice,
                          command=selection,
                          value=2)
with_lowers.grid(sticky=W, row=5, column=2, padx=40)

with_symbols = Radiobutton(text='Symbols',
                           bg='#5F4843',
                           fg='black',
                           variable=choice,
                           command=selection,
                           value=3)
with_symbols.grid(sticky=W, row=6, column=2, padx=40)

with_numbers = Radiobutton(text='Numbers',
                           bg='#5F4843',
                           fg='black',
                           variable=choice,
                           command=selection,
                           value=4)
with_numbers.grid(sticky=W, row=7, column=2, padx=40)

button_generate = Button(text='Generate',
                         cursor='watch',
                         activebackground='#FCBDA4',
                         bg='#a0a0a0', command=generate_password)
button_generate.grid(sticky=W, row=8, column=1, padx=20, pady=40)
# password = str(generate_password)

password_field = Label(window, text='')
password_field.grid(row=8, columnspan=3, sticky=E
                    )

button_quit = Button(text='Quit',
                     cursor='watch',
                     activebackground='#FCBDA4',
                     bg='#a0a0a0', command=window.destroy
                     )
button_quit.grid(sticky=W, row=9, column=1, padx=30)

text_editor = Label(text='Edit by Aslan', bg='#5F4843',
                    font='Times 20')

text_editor.grid(row=10, column=2)

# logic

upper = string.ascii_uppercase + string.ascii_letters
lower = string.ascii_lowercase + string.ascii_letters

symbols_elem = """!@#$%^&*():"{}|?><"""
symbols = string.ascii_letters + symbols_elem

numbers = string.digits + string.hexdigits


window.mainloop()
