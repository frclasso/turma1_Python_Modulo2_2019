
from tkinter import *

root = Tk()
root.title("PainedWindow")

m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)

left = Entry(m1, bd=2)
m1.add(left)


m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)


top = Scale(m2, orient=HORIZONTAL)
m2.add(top)

button = Button(m2, text="ok")
m2.add(button)
root.mainloop()
