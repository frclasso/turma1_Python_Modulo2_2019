
from tkinter import *

root = Tk()
root.title("Canvas")
# canvas
# Canvas é filho de root
C = Canvas(root,bg='yellow', height=250, width=300)
C.pack()

# arco
coord = 10,50,240,210
arc = C.create_arc(coord, start=0, extent=150, fill='red')

# linha
line = C.create_line(10,10,200,200, fill='blue')
root.mainloop()