from tkinter import *
from tkinter import messagebox
import string
import random

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title('PyPassword Manager')
        self.config(padx=50, pady=50)

        self.home_screen()

    def home_screen(self):
        canvas = Canvas(width=200, height=200)
        img = PhotoImage(file='logo.png')
        canvas.create_image(100, 94, image=img)
        canvas.grid(row=0, column=1)

        lbl_website = Label(text='Website :')
        lbl_website.grid(row=1, column=0)
        lbl_username = Label(text='Username :')
        lbl_username.grid(row=2, column=0)
        lbl_password = Label(text='Password :')
        lbl_password.grid(row=3, column=0)

        self.input_website = Entry(width=45,)
        self.input_website.grid(row=1, column=1, columnspan=2, pady=2)
        self.input_website.focus()
        self.input_username = Entry(width=45)
        self.input_username.insert(0, 'daine.bigham@gmail.com')
        self.input_username.grid(row=2, column=1, columnspan=2, pady=2)
        self.input_password = Entry(width=34)
        self.input_password.grid(row=3, column=1, pady=2)

        self.btn_password = Button(text=' Generate ', command=self.generate_password)
        self.btn_password.grid(row=3, column=2, pady=2)
        self.btn_add = Button(text='Add', width=38, command=self.save)
        self.btn_add.grid(row=4, column=1, columnspan=2, pady=2)

        self.mainloop()
    
    def save(self):

        website = self.input_website.get()
        username = self.input_username.get()
        password = self.input_password.get()

        if len(website) == 0 or len(password) == 0: 
            messagebox.showinfo(title='Oops...', message="Looks like you're missing something")
        else: 
            is_ok = messagebox.askokcancel(title=website, message=f'Are you sure?\nUsername: {username}\nPassword: {password}')

            if is_ok:
                with open('data.txt', 'a') as f:
                    f.write(f'{website} | {username} | {password}\n')

                    self.input_website.delete(0, END)
                    self.input_password.delete(0, END)