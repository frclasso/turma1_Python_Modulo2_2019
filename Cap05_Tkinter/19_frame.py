
from tkinter import *

root = Tk()
root.title("Label Frame")

labelFrame = LabelFrame(root, text='This is a LabelFrame')
labelFrame.pack(fill='both', expand='yes')

left = Label(labelFrame, text="Inside the LabelFrame")
left.pack()

root.mainloop()