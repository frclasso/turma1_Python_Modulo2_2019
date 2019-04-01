from tkinter import *
from tkinter import ttk

root = Tk()

button = ttk.Button(root, text='Click me')
button.pack()

def callback():
    print('Clicked')

button.config(command=callback)

button.invoke()  # print clicked

logo = PhotoImage(file='python_logo.gif')
button.config(ima=logo, compound=LEFT)

small_logo = logo.subsample(4,4)
button.config(image=small_logo)

root.mainloop()