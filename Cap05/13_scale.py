
from tkinter import *

root = Tk()
root.title("Scale widget")

def sel():
    selection = "Value = " + str(var.get())
    label.config(text=selection)

var = DoubleVar() # float
scale = Scale(root, variable=var)
scale.pack(anchor=CENTER)

button = Button(root, text='Get scale value', command=sel)
button.pack(anchor=CENTER)

label = Label(root)
label.pack()

root.mainloop()