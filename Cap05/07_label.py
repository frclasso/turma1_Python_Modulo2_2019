
from tkinter import *

root = Tk()
root.title("Label")

label = Label(root, text='Hey, How are you doing?', relief=RAISED)
label.pack()

root.mainloop()