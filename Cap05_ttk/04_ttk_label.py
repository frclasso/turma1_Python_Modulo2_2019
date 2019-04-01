from tkinter import *
from tkinter import ttk

root = Tk()

label = ttk.Label(root, text='Hello , Tkinter!')
label.pack()

#label.config(text='Howdy, Tkinter')
label.config(text='Howdy, Tkinter Great to see you again')

label.config(wraplength=150)
label.config(justify=CENTER)

# alterar cor
label.config(foreground='blue', background='black')
# alterar fonte
label.config(font=('Courier', 18, 'bold'))

#label.config(text='Howdy, Tkinter!')
label.config(compound='text')
label.config(compound='center')
label.config(compound='left')

root.mainloop()