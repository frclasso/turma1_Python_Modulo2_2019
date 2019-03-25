
from tkinter import *

root = Tk()

root.title("Entry function")

l1 = Label(root, text="User name:")
l1.pack(side=LEFT)

e1 = Entry(root, bd=2)
e1.pack(side=RIGHT)

root.mainloop()