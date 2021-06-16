from tkinter import *

window = Tk()
window.title('PyPassword Manager')
window.config(padx=50, pady=50)

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

input_website = Entry(width=45,)
input_website.grid(row=1, column=1, columnspan=2, pady=2)
input_username = Entry(width=45)
input_username.grid(row=2, column=1, columnspan=2, pady=2)
input_password = Entry(width=34)
input_password.grid(row=3, column=1, pady=2)

btn_password = Button(text=' Generate ')
btn_password.grid(row=3, column=2, pady=2)
btn_add = Button(text='Add', width=38)
btn_add.grid(row=4, column=1, columnspan=2, pady=2)

window.mainloop()
