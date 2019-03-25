
from tkinter import *

root = Tk()
root.title("Text")

text = Text(root)

text.insert(INSERT, "Hello Tkinter World...")
text.insert(END, "Bye bye...")
text.pack()

text.tag_add('here', '1.0', '1.4')
text.tag_add('start', '1.8', '1.13')
text.tag_config('here', background='yellow', foreground='blue')
text.tag_config('start', background='red', foreground='green')
root.mainloop()