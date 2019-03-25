
from tkinter import *

root = Tk()
root.title("Frame and Button")

frame = Frame(root)
frame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

redbutton = Button(frame, text='Red', fg='red')
redbutton.pack(side=LEFT)

greenbutton = Button(frame, text='Green', fg='green')
greenbutton.pack(side=LEFT)

bluebutton = Button(bottomFrame, text='Blue', fg='blue')
bluebutton.pack(side=LEFT)

blackbutton = Button(bottomFrame, text='Black', fg='black')
blackbutton.pack(side=LEFT)

root.mainloop()