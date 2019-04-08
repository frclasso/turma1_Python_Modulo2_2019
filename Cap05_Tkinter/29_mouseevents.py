
from tkinter import *

root = Tk()

root.title("Mouse events")

def left_click(event):
    Label(root, text="Left click").pack()

def middle_click(event):
    Label(root, text="Middle click").pack()

def right_click(event):
    Label(root, text="Right click").pack()


root.bind_all("<Button-1>", left_click)
root.bind_all("<Button-2>", middle_click)
root.bind_all("<Button-3>", right_click)

root.mainloop()