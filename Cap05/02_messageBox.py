
from tkinter import *
from tkinter import messagebox


root = Tk()

# W x H + Left + Top
root.geometry('120x80+100+100')

# messageBox


def CallBack():
    messagebox.showinfo(title='Hello Tkinter',message='Hello World')


B = Button(root, text="Hello", command=CallBack)
B.place(x=50, y=50)

root.mainloop()