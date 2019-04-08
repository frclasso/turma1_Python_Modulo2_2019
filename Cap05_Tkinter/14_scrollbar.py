
from tkinter import *

root = Tk()
root.title("ScrollBar")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

myList = Listbox(root, yscrollcommand=scrollbar.set)

for line in range(50):
    myList.insert(END, 'This is line number: '+ str(line))

myList.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=myList.yview)

root.mainloop()