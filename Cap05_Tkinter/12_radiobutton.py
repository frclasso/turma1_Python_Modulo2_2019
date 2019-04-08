
from tkinter import *

root = Tk()
root.title("Radio Button")

def sel():
    selection = "You selected the option "+ str(var.get())
    label.config(text=selection)

var = IntVar()

r1 = Radiobutton(root, text='Option 1', variable=var, value=1, command=sel)
r1.pack(anchor=W)

r2 = Radiobutton(root, text='Option 2', variable=var, value=2, command=sel)
r2.pack(anchor=W)

r3 = Radiobutton(root, text='Option 3', variable=var, value=3, command=sel)
r3.pack(anchor=W)

label = Label(root)
label.pack()

root.mainloop()