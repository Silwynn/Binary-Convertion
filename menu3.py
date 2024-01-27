from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('MeNU 3')
root.geometry('500x300')

binary = StringVar()
lbldecimal = StringVar()
lblhexa = StringVar()
lbloctal = StringVar()

def convert():
    try:
        num = int(binary.get(), 2)
        lbldecimal.set(str(num))
        lblhexa.set(hex(num)[2:])
        lbloctal.set(oct(num)[2:])
    except ValueError:
        messagebox.showerror('Error', 'You must enter a valid binary number to convert')

def clear():
    binary.set('')
    lblhexa.set('')
    lbldecimal.set('')
    lbloctal.set('')
    
def exit_app():
    if messagebox.askyesno('Exit', 'Do you really want to exit?'):
        root.destroy()

Label(root, text='Conversion System', font=('times new roman', 40, 'bold'), bg='lime', fg='blue', relief=RIDGE).pack(pady=10)
   
n = Label(root, text='Input Binary', font=('times new roman', 15, 'bold'), fg='blue')
n.place(x=300, y=150)

d = Label(root, text='Decimal', font=('times new roman', 15, 'bold'), fg='blue')
d.place(x=300, y=230)

h = Label(root, text='Hexa Decimal', font=('times new roman', 15, 'bold'), fg='blue')
h.place(x=300, y=300)

o = Label(root, text='Octa Decimal', font=('times new roman', 15, 'bold'), fg='blue')
o.place(x=300, y=370)

e1 = Entry(root, font='arial 20', fg='blue', justify=CENTER, relief=GROOVE, textvariable=binary)
e1.place(x=650, y=150)

e2 = Entry(root, font='arial 20', fg='blue', justify=CENTER, relief=GROOVE, textvariable=lbldecimal)
e2.place(x=650, y=230)

e3 = Entry(root, font='arial 20', fg='blue', justify=CENTER, relief=GROOVE, textvariable=lblhexa)
e3.place(x=650, y=300)

e4 = Entry(root, font='arial 20', fg='blue', justify=CENTER, relief=GROOVE, textvariable=lbloctal)
e4.place(x=650, y=370)

btn1 = Button(root, text='Convert', font='arial 20 bold', fg='crimson', bg='lime', width=10, command=convert)
btn1.place(x=300, y=580)

btn2 = Button(root, text='Clear', font='arial 20 bold', fg='crimson', bg='lime', width=10, command=clear)
btn2.place(x=600, y=580)

btn3 = Button(root, text='Exit', font='arial 20 bold', fg='crimson', bg='lime', width=10, command=exit_app)
btn3.place(x=900, y=580)
root.mainloop()
