
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Alert message")

messagebox.showinfo(title='Alert message',
                    message='This is just a alert message')

response=messagebox.askquestion(title='Simple question',
                                 message='Do you love Python?')

if response == 'yes':
    Label(window, text='Yeah, you love Python').pack()
else:
    Label(window, text="You don't love Python").pack()


window.mainloop()

