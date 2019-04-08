
from tkinter import *

root = Tk()
root.title("spinbox")

s = Spinbox(root, from_=0, to=10)
s.pack()

root.mainloop()