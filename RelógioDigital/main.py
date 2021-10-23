from tkinter import *
from datetime import datetime
from utils import pickColor

import pyglet
pyglet.font.add_file('RelógioDigital\digital-7.ttf')

def clockTime():
    time = datetime.now()
    hour = time.strftime('%H:%M:%S')
    weekDay = time.strftime('%A')
    dateDay = time.day
    mounth = time.strftime('%b')
    year = time.strftime('%Y')

    label1.config(text=hour)
    label1.after(200, clockTime)
    
    label2.config(text=weekDay + ' ' + str(dateDay) + '/' + str(mounth) + '/' + year)


bgColor = pickColor.colorBlack
textColor = pickColor.colorGreen

tk = Tk()
tk.title('Relógio Digital')
tk.geometry('440x200')
tk.resizable(False, False)

tk.iconbitmap('RelógioDigital\clock.ico')

def lightMode():
    bgColor = pickColor.colorWhite
    tk.config(bg=bgColor)
    label1.config(bg=bgColor)
    label2.config(bg=bgColor)

    textColor = pickColor.colorBlack
    label1.config(fg=textColor)
    label2.config(fg=textColor)


def darkMode():
    bgColor = pickColor.colorBlack
    tk.config(bg=bgColor)
    label1.config(bg=bgColor)
    label2.config(bg=bgColor)

    textColor = pickColor.colorWhite
    label1.config(fg=textColor)
    label2.config(fg=textColor)


def regularMode():
    bgColor = pickColor.colorBlack
    tk.config(bg=bgColor)
    label1.config(bg=bgColor)
    label2.config(bg=bgColor)

    textColor = pickColor.colorGreen
    label1.config(fg=textColor)
    label2.config(fg=textColor)


menuBar = Menu(tk)
optionsMenuBar = Menu(tk, tearoff=0)
menuBar.add_cascade(label='Opçoes', menu=optionsMenuBar)

optionChangeColor = Menu(tk, tearoff=0)
optionChangeColor.add_command(label='Light Mode', command=lightMode)
optionChangeColor.add_command(label='Dark Mode', command=darkMode)
optionChangeColor.add_command(label='Padrão', command=regularMode)
optionsMenuBar.add_cascade(label='Tema', menu=optionChangeColor)


optionsMenuBar.add_separator()
optionsMenuBar.add_command(label='Sair', command=tk.quit)

tk.configure(background=bgColor, menu=menuBar)

label1 = Label(tk, font=('digital-7', 100), bg=bgColor, fg=textColor, width=7)
label1.grid(row=0, column=0, sticky=N)

label2 = Label(tk, font=('digital-7', 20), bg=bgColor, fg=textColor)
label2.grid(row=1, column=0, sticky=N)


clockTime()
tk.mainloop()
