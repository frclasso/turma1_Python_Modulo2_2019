
from tkinter import *
from tkinter import ttk
from tkinter import messagebox



class FeedBack:

    def __init__(self, master):
        self.header_frame = ttk.Frame(master)
        self.header_frame.pack()
        self.logo = PhotoImage(file='tour_logo.gif')
        ttk.Label(self.header_frame, image=self.logo).grid(row=0,
                                                           column=0,
                                                           rowspan=2)
        ttk.Label(self.header_frame, text='Thanks for exploring').grid(row=0,column=1)
        ttk.Label(self.header_frame, wraplength=300,
                  text=("We're glad you chose Explore California "
                        "for you recente adventure."
                        "Please tell us what you tought about "
                        "the 'Desert to sea' tour.")).grid(row=1, column=1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text='Name: ').grid(row=0, column=0, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text='Email: ').grid(row=0, column=1,padx=5,sticky='sw')
        ttk.Label(self.frame_content, text='Comments: ').grid(row=2, column=0,padx=5,sticky='sw')

        self.entry_name = ttk.Entry(self.frame_content, width=24)
        self.entry_email = ttk.Entry(self.frame_content, width=24)
        self.entry_comments = Text(self.frame_content, width=50, height=10)

        self.entry_name.grid(row=1, column=0, padx=5)
        self.entry_email.grid(row=1, column=1, padx=5)
        self.entry_comments.grid(row=3, column=0, columnspan=2, padx=5)

        ttk.Button(self.frame_content, text='Submit').grid(row=4, column=0,padx=5, sticky='e')
        ttk.Button(self.frame_content, text='Clear').grid(row=4, column=1, padx=5, sticky='e')


    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Coments: {}'.format(self.entry_comments.get(1.0, 'end')))
        self.clear()
        messagebox.showinfo(title='Explore California Feed Back',
                            message='Comments Submitted!')

    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.entry_comments.delete(1.0, 'end')


def main():
    root = Tk()
    feedback = FeedBack(root)
    root.mainloop()


if __name__=="__main__":main()