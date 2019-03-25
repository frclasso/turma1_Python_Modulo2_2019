from tkinter import *

root = Tk()

lb1 = Listbox(root)
lb1.insert(1, 'Python')
lb1.insert(2, 'Perl')
lb1.insert(3, 'Go')
lb1.insert(4, 'C#')
lb1.insert(5, 'PHP')
lb1.insert(6, 'Django')
lb1.insert(7, 'Julia lang')

lb1.pack()

root.mainloop()