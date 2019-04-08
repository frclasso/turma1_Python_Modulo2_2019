
from tkinter import *
from PIL import Image
from PIL import ImageTk

window = Tk()
window.title("Images and incons")

icon = Image.open('python_logo.png')
icon = icon.resize((300,200), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(icon)
Label(window, image=photoImg).grid(row= 0, column=0)

window.mainloop()