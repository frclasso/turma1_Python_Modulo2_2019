
from tkinter import *

root = Tk()
root.title("Menu Button")

mb = Menubutton(root, text='Condiments', relief=RAISED)

mb.grid()

mb_menu = Menu(mb, tearoff=0)
mb['menu'] = mb_menu

mayoVar = IntVar()
ketchVar = IntVar()

mb_menu.add_checkbutton(label='Mayo', variable=mayoVar)
mb_menu.add_checkbutton(label='Ketchup', variable=ketchVar)

mb.pack()

root.mainloop()