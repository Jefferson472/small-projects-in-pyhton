from tkinter import *
from datetime import datetime
from utils import pickColor


# Pyglet simplesmente parou de funcionar, FileNotFoundError: [Errno 2] No such file or directory: 'fonts\\digital-7.ttf'.
# O comando font = open(font, 'rb') também não funcionou mais.
# import pyglet
# pyglet.font.add_file('digital-7.ttf')


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
tk.geometry('440x180')
tk.resizable(False, False)

# tk.iconbitmap('clock.ico')

def changeColorBg():
    print('alterou a cor')
    tk.quit()
    bgColor = pickColor.colorBlue    
    tk.configure(background=bgColor, menu=menuBar)
    tk.mainloop()
    


def changeColorText():
    print('alterou a cor')


def exitApp():
    tk.quit()


menuBar = Menu(tk)
optionsMenuBar = Menu(tk, tearoff=0)
optionsMenuBar.add_command(label='Cor de Fundo', command=changeColorBg)
optionsMenuBar.add_command(label='Cor da Fonte', command=changeColorText)
optionsMenuBar.add_separator()
optionsMenuBar.add_command(label='Sair', command=exitApp)
menuBar.add_cascade(label='Opçoes', menu=optionsMenuBar)

tk.configure(background=bgColor, menu=menuBar)

label1 = Label(tk, font=('digital-7 100'), bg=bgColor, fg=textColor)
label1.grid(row=0, column=0, sticky=N, padx=5)

label2 = Label(tk, font=('digital-7 20'), bg=bgColor, fg=textColor)
label2.grid(row=1, column=0, sticky=N, padx=5)

label3 = Label(tk, font=('Arial 5'), bg=bgColor, fg=textColor, text='Por Jefferson Miranda', pady=0)
label3.grid(row=3, column=0, sticky=E)


clockTime()
tk.mainloop()
