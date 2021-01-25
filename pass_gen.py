import tkinter as tk
from tkinter import *
from tkinter import HORIZONTAL
import secrets
import time
from tkinter import messagebox
from random import randint


def generate_password(digit):
    count_length = get_value_length(digit)
    password = secrets.token_urlsafe(count_length)
    return password


def get_value_length(digit):
    print(digit)
    return int(digit)


def get_upper():
    upper = lambda: print(a.get())
    return upper


def get_lower():
    lower = lambda: print(b.get())
    return lower


def get_numbers():
    numbers = lambda: print(c.get())
    return numbers


def get_symbols():
    symbols = lambda: print(d.get())
    return symbols


window = tk.Tk()

window.geometry(f'470x420+100+200')
window.resizable(False, False)
window['bg'] = '#5F4843'
window.title('Password generator')
choose_length = Label(window,
                      text='Choose length of password:',
                      fg='black', bg='#5F4843', justify=LEFT,
                      font="Arial 11", relief=RIDGE
                      )
choose_length.grid(row=2, column=1, padx=20, pady=10, sticky=W)

scale_length = Scale(window, orient=HORIZONTAL,
                     bg='#5F4843', fg='black',
                     to=15, command=get_value_length
                     )
scale_length.grid(row=2, column=4, pady=10)

choose_symbols = Label(window,
                       text='Choose symbols of your password:',
                       fg='black', bg='#5F4843', justify=LEFT,
                       font="Arial 11", relief=RIDGE
                       )
choose_symbols.grid(row=3, column=1, padx=20, pady=40, sticky=W)

a = tk.BooleanVar()
b = tk.BooleanVar()
c = tk.BooleanVar()
d = tk.BooleanVar()
upper_checkbox = Checkbutton(text='Upper case',
                             bg='#5F4843', fg='black', variable=a, command=get_upper())


upper_checkbox.grid(sticky=W, row=4, column=4, padx=40)

lower_checkbox = Checkbutton(text='Lower case',
                             bg='#5F4843', fg='black', variable=b, command=get_lower())
lower_checkbox.grid(sticky=W, row=5, column=4, padx=40)

numbers = Checkbutton(text='Numbers',
                      bg='#5F4843', fg='black', variable=c, command=get_numbers())
numbers.grid(sticky=W, row=6, column=4, padx=40)

special_symbols = Checkbutton(text='Special symbols',
                              bg='#5F4843', fg='black', variable=d, command=get_symbols())
special_symbols.grid(sticky=W, row=7, column=4, padx=40)

button_generate = Button(text='Generate',
                         cursor='watch',
                         activebackground='#FCBDA4',
                         bg='#a0a0a0', command=generate_password)
button_generate.grid(sticky=W, row=8, column=1, padx=20, pady=40)

field_generating = Entry(text='Generated password',
                         state="readonly")
field_generating.grid(row=8, column=4)

button_quit = Button(text='Quit',
                     cursor='watch',
                     activebackground='#FCBDA4',
                     bg='#a0a0a0', command=window.destroy
                     )
button_quit.grid(sticky=W, row=9, column=1, padx=30, )

text_editor = Label(text='Delal Aslan celih minut 40\n'
                         'potom poshel kushat', bg='#5F4843',
                    font='Times 10')
text_editor.grid(row=9, column=4)

window.mainloop()
