
from tkinter import *

window = Tk()
window.title("DropDown Menu")


def function():
    pass

# menu principal
root_menu = Menu(window)
window.config(menu = root_menu)

# sub menu 1
file_menu = Menu(root_menu)
file_menu.add_command(label='New File', command=function)
file_menu.add_command(label='Open File', command=function)

file_menu.add_separator()# cria linha para separar
file_menu.add_command(label='Exit', command=window.quit)

root_menu.add_cascade(label='File', menu=file_menu)

# sub menu 2
edit_menu = Menu(root_menu)
edit_menu.add_command(label='Undo', command=function)
edit_menu.add_command(label='Redo', command=function)

root_menu.add_cascade(label='Edit', menu=edit_menu)


window.mainloop()