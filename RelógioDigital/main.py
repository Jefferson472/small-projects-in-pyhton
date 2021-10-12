from tkinter import *
from datetime import datetime
import pyglet

font = 'fonts\digital-7.ttf'
digitalFont = open(font, 'rb')

pyglet.font.add_file('fonts\digital-7.ttf')

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


colorBlack = "#3d3d3d"
colorWhite = "#fafcff"
colorGreen = "#21c25c"
colorRed = "#eb463b"
colorAsh = "#dedcdc"
colorBlue = "#3080f0"

bgColor = colorBlack


tk = Tk()
tk.title('Relógio Digital')
tk.geometry('440x180')
tk.resizable(False, False)
tk.configure(background=bgColor)

label1 = Label(tk, text='', font=('digital-7 80'), bg=bgColor, fg=colorGreen)
label1.grid(row=0, column=0, sticky=NW, padx=5)

label2 = Label(tk, font=('digital-7 20'), bg=bgColor, fg= colorGreen)
label2.grid(row=1, column=0, sticky=NW, padx=5)

clockTime()


tk.mainloop()
