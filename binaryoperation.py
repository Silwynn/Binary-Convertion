from tkinter import *
from tkinter import messagebox

def perform_binary_operation(operation, operand1, operand2=None):
    try:
        operand1 = int(operand1, 2)
        if operand2:
            operand2 = int(operand2, 2)
    except ValueError:
        messagebox.showerror('Error', 'Invalid binary input')
        return None

    if operation == 'Division':
        if operand2 == 0:
            messagebox.showerror('Error', 'Cannot divide by zero')
            return None
        else:
            return bin(operand1 // operand2)[2:]
    elif operation == 'Multiplication':
        return bin(operand1 * operand2)[2:]
    elif operation == 'Subtraction':
        return bin(operand1 - operand2)[2:]
    elif operation == 'Addition':
        return bin(operand1 + operand2)[2:]
    elif operation == '2s Complement':
        return bin(-operand1)[2:]
    else:
        messagebox.showerror('Error', 'Invalid operation')
        return None

def calculate_result():
    operation = operation_var.get()
    operand1 = entry_operand1.get()
    operand2 = entry_operand2.get()

    result = perform_binary_operation(operation, operand1, operand2)

    if result is not None:
        messagebox.showinfo('Result', f'Result: {result}')

root = Tk()
root.title('Binary Operations')
root.geometry('500x300')

operation_var = StringVar()
operation_var.set('Division')

label_heading = Label(root, text='Binary Operations', font=('times new roman', 20, 'bold'), bg='lime', fg='blue', relief=RIDGE)
label_heading.pack(pady=10)

label_operation = Label(root, text='Select Operation:', font=('times new roman', 15, 'bold'), fg='blue')
label_operation.place(x=20, y=70)

options = ['Division', 'Multiplication', 'Subtraction', 'Addition', '2s Complement']
dropdown_operation = OptionMenu(root, operation_var, *options)
dropdown_operation.place(x=200, y=65)

label_operand1 = Label(root, text='Operand 1:', font=('times new roman', 15, 'bold'), fg='blue')
label_operand1.place(x=20, y=120)

entry_operand1 = Entry(root, font='arial 15', fg='blue', justify=CENTER)
entry_operand1.place(x=200, y=115)

label_operand2 = Label(root, text='Operand 2:', font=('times new roman', 15, 'bold'), fg='blue')
label_operand2.place(x=20, y=170)

entry_operand2 = Entry(root, font='arial 15', fg='blue', justify=CENTER)
entry_operand2.place(x=200, y=165)

btn_calculate = Button(root, text='Calculate', font='arial 15 bold', fg='crimson', bg='lime', width=15, command=calculate_result)
btn_calculate.place(x=150, y=220)

root.mainloop()
