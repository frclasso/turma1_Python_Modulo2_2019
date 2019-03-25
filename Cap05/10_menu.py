
from tkinter import *

root = Tk()
root.title("Menu")

menuBar = Menu(root)

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text='Click here!!!')
    button.pack()

# file menu
filemenu = Menu(menuBar, tearoff=0)
filemenu.add_command(label='New', command=donothing)
filemenu.add_command(label='Open', command=donothing)
filemenu.add_command(label='Save', command=donothing)
filemenu.add_command(label='Save As', command=donothing)
filemenu.add_command(label='Close', command=root.quit)
filemenu.add_separator()

filemenu.add_command(label='Exit', command=root.quit)
menuBar.add_cascade(label='File', menu=filemenu)

#edit menu
edit_menu = Menu(menuBar, tearoff=0)
edit_menu.add_command(label='Undo', command=donothing)
edit_menu.add_separator()

edit_menu.add_command(label='Cut', command=donothing)
edit_menu.add_command(label='Copy', command=donothing)
edit_menu.add_command(label='Paste', command=donothing)
edit_menu.add_command(label='Delete', command=donothing)
edit_menu.add_command(label='Select All', command=donothing)
menuBar.add_cascade(label='Edit', menu=edit_menu)

#help menu
help_menu = Menu(menuBar, tearoff=0)
help_menu.add_command(label='Help index', command=donothing)
help_menu.add_command(label='About', command=donothing)
menuBar.add_cascade(label='Help', menu=help_menu)

root.config(menu=menuBar)
root.mainloop()