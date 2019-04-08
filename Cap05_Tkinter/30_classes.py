#!/usr/bin/env python3

# -*-coding:utf-8 -*-

from tkinter import *

# Tk() - root, window, janela, tk
root = Tk()
root.title('GeeksBro Class')


class GeeksBro:
    def __init__(self, root):
        self.text_btn = Button(root, text='Click me',command=self.say_hi)
        self.text_btn.pack() # gerencidor de layout

        self.close_btn = Button(root, text='Close', command=root.quit)
        self.close_btn.pack()

    def say_hi(self):
        Label(root, text='Hi!').pack()


geeks_bro = GeeksBro(root)

root.mainloop()