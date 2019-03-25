
from tkinter import *

root = Tk()
root.title('Place method')

l1 = Label(root, text='Physics')
l1.place(x=10, y=10)
e1 = Entry(root, bd=2)
e1.place(x=70, y=10)

l2 = Label(root, text='Maths')
l2.place(x=10, y=50)
e2 = Entry(root, bd=2)
e2.place(x=70, y=50)

l3 = Label(root, text='Total')
l3.place(x=10, y=150)
e3 = Entry(root, bd=2)
e3.place(x=70, y=150)


B = Button(root, text="Add")
B.place(x=100, y=100)

root.geometry('280x260+10+10')
root.mainloop()