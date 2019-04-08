
from tkinter import *

root = Tk()
root.title("Label and fill")

Label(root, text="Sufficient Width", fg="white", bg="purple").pack()
Label(root, text="Width of x", fg="white", bg="green").pack(fill='x')
Label(root, text="Height of y",
      fg="white", bg="black").pack(fill='y', side=LEFT)

root.mainloop()