import tkinter as tk
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

def convert():
    try:
        binary_input = binary.get()
        if not binary_input:
            raise ValueError("Empty input")
        
        num = int(binary_input, 2)
        lbldecimal.set(str(num))
        lblhexa.set(hex(num)[2:])
        lbloctal.set(oct(num)[2:])
    except ValueError as e:
        messagebox.showerror('Error', 'You must enter a valid binary number to convert')

def clear():
    binary.set('')
    lblhexa.set('')
    lbldecimal.set('')
    lbloctal.set('')
    
def exit_app():
    if messagebox.askyesno('Exit', 'Do you really want to exit?'):
        root.destroy()

def Menu_2_page():
    hide_indicators()  
    Menu_2_indicate.config(bg='#158aff')
    delete_pages()
    
    def show_decimal():
        try:
            binary_input = entry_operand1.get()
            if not binary_input:
                raise ValueError("Empty input")
            
            num = int(binary_input, 2)
            messagebox.showinfo('Decimal Value', f'Decimal Value: {num}')
        except ValueError as e:
            messagebox.showerror('Error', 'You must enter a valid binary number to convert')

    Menu_2_frame = tk.Frame(main_frame)
    
    label_heading = tk.Label(Menu_2_frame, text='Binary Operations', font=('times new roman', 20, 'bold'), bg='lime', fg='blue', relief=tk.RIDGE)
    label_heading.pack(pady=10)
    
    label_operation = tk.Label(Menu_2_frame, text='Select Operation:', font=('times new roman', 15, 'bold'), fg='blue')
    label_operation.pack()

    options = ['Division', 'Multiplication', 'Subtraction', 'Addition', '2s Complement']
    dropdown_operation = tk.OptionMenu(Menu_2_frame, operation_var, *options)
    dropdown_operation.pack()

    label_operand1 = tk.Label(Menu_2_frame, text='Operand 1:', font=('times new roman', 15, 'bold'), fg='blue')
    label_operand1.pack()

    global entry_operand1 
    entry_operand1 = tk.Entry(Menu_2_frame, font='arial 15', fg='blue', justify=tk.CENTER)
    entry_operand1.pack()

    label_operand2 = tk.Label(Menu_2_frame, text='Operand 2:', font=('times new roman', 15, 'bold'), fg='blue')
    label_operand2.pack()

    global entry_operand2  # Define entry_operand2 as a global variable
    entry_operand2 = tk.Entry(Menu_2_frame, font='arial 15', fg='blue', justify=tk.CENTER)
    entry_operand2.pack()

    btn_calculate = tk.Button(Menu_2_frame, text='Calculate', font='arial 15 bold', fg='crimson', bg='lime', width=15, command=calculate_result)
    btn_calculate.pack(pady=10)

    btn_show_decimal = tk.Button(Menu_2_frame, text='Show Decimal', font='arial 15 bold', fg='crimson', bg='lime', width=15, command=show_decimal)
    btn_show_decimal.pack(pady=10)

    Menu_2_frame.pack(pady=20)

def Menu_3_page():
    hide_indicators()  
    Menu_3_indicate.config(bg='#158aff')
    delete_pages()
    
    Menu_3_frame = tk.Frame(main_frame)
    
    label_heading = tk.Label(Menu_3_frame, text='Conversion System', font=('times new roman', 40, 'bold'), bg='lime', fg='blue', relief=tk.RIDGE)
    label_heading.pack(pady=10)
    
    input_frame = tk.Frame(Menu_3_frame)
    input_frame.pack(pady=10)

    label_input_binary = tk.Label(input_frame, text='Input Binary', font=('times new roman', 15, 'bold'), fg='blue')
    label_input_binary.grid(row=0, column=0, padx=10, pady=5, sticky='w')

    global binary, lbldecimal, lblhexa, lbloctal  
    
    binary = tk.StringVar()  
    lbldecimal = tk.StringVar()
    lblhexa = tk.StringVar()
    lbloctal = tk.StringVar()

    entry_binary = tk.Entry(input_frame, font='arial 20', fg='blue', justify=tk.CENTER, relief=tk.GROOVE, textvariable=binary)
    entry_binary.grid(row=0, column=1, padx=10, pady=5)

    btn_convert = tk.Button(input_frame, text='Convert', font='arial 15 bold', fg='crimson', bg='lime', width=10, command=convert)
    btn_convert.grid(row=0, column=2, padx=10, pady=5)

    result_frame = tk.Frame(Menu_3_frame)
    result_frame.pack(pady=10)

    label_decimal = tk.Label(result_frame, text='Decimal', font=('times new roman', 15, 'bold'), fg='blue')
    label_decimal.grid(row=0, column=0, padx=10, pady=5, sticky='w')

    entry_decimal = tk.Entry(result_frame, font='arial 20', fg='blue', justify=tk.CENTER, relief=tk.GROOVE, textvariable=lbldecimal)
    entry_decimal.grid(row=0, column=1, padx=10, pady=5)

    label_hexa_decimal = tk.Label(result_frame, text='Hexa Decimal', font=('times new roman', 15, 'bold'), fg='blue')
    label_hexa_decimal.grid(row=1, column=0, padx=10, pady=5, sticky='w')

    entry_hexa_decimal = tk.Entry(result_frame, font='arial 20', fg='blue', justify=tk.CENTER, relief=tk.GROOVE, textvariable=lblhexa)
    entry_hexa_decimal.grid(row=1, column=1, padx=10, pady=5)

    label_octa_decimal = tk.Label(result_frame, text='Octa Decimal', font=('times new roman', 15, 'bold'), fg='blue')
    label_octa_decimal.grid(row=2, column=0, padx=10, pady=5, sticky='w')

    entry_octa_decimal = tk.Entry(result_frame, font='arial 20', fg='blue', justify=tk.CENTER, relief=tk.GROOVE, textvariable=lbloctal)
    entry_octa_decimal.grid(row=2, column=1, padx=10, pady=5)

    btn_clear = tk.Button(Menu_3_frame, text='Clear', font='arial 15 bold', fg='crimson', bg='lime', width=10, command=clear)
    btn_clear.pack(pady=10, side=tk.LEFT)

    
    Menu_3_frame.pack(pady=20)


def indicate(lb, page):
    hide_indicators()  
    lb.config(bg='#158aff')
    delete_pages()
    page()

def home_page():
    home_frame = tk.Frame(main_frame)
    home_frame.pack(pady=20)
    
    lb = tk.Label(home_frame, text='BINARY CONVERSION\n\n', font=('Bold', 30))
    lb.pack()

    title_lb = tk.Label(home_frame, text='Binary operation and Conversion by Mark Silwyn Jardin and El Cid de Guzman', font=('Arial', 14))
    title_lb.pack()
    
    home_frame.pack(pady=20)

def Menu_1_page():
    Menu_1_frame = tk.Frame(main_frame)
    
    lb = tk.Label(Menu_1_frame, text='Main Menu', font=('Bold', 30))
    lb.pack()
    
    btn_exit = tk.Button(Menu_1_frame, text='Exit', font='arial 15 bold', fg='crimson', bg='lime', width=10, command=exit_app)
    btn_exit.pack(pady=10, side=tk.RIGHT)
    
    btn_exit = tk.Button(Menu_1_frame, text='Menu 3', font='arial 15 bold', fg='crimson', bg='lime', width=10, command=Menu_3_page)
    btn_exit.pack(pady=10, side=tk.RIGHT)
    
    btn_exit = tk.Button(Menu_1_frame, text='Menu 2', font='arial 15 bold', fg='crimson', bg='lime', width=10, command=Menu_2_page)
    btn_exit.pack(pady=10, side=tk.RIGHT)
    
    Menu_1_frame.pack(pady=20)

    
    Menu_1_frame.pack(pady=20)

def hide_indicators():
    home_indicate.config(bg='#c3c3c3')
    Menu_1_indicate.config(bg='#c3c3c3')
    Menu_2_indicate.config(bg='#c3c3c3')
    Menu_3_indicate.config(bg='#c3c3c3')
    
def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

root = tk.Tk()
root.title("Binary Conversion")
root.geometry('825x500')

options_frame = tk.Frame(root, bg="#c3c3c3")

home_btn = tk.Button(options_frame, text='Home', font=('Bold', 15),
                     fg='#158aff', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(home_indicate, home_page))

home_btn.place(x=10, y=50)

home_indicate = tk.Label(options_frame, text=" ", bg="#c3c3c3")
home_indicate.place(x=3, y=50, width=5, height=40)

Menu_1_btn = tk.Button(options_frame, text='Menu 1', font=('Bold', 15),
                     fg='#158aff', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(Menu_1_indicate, Menu_1_page))

Menu_1_btn.place(x=10, y=100)

Menu_1_indicate = tk.Label(options_frame, text=" ", bg="#c3c3c3")
Menu_1_indicate.place(x=3, y=100, width=5, height=40)

Menu_2 = tk.Button(options_frame, text='Menu 2', font=('Bold', 15),
                     fg='#158aff', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(Menu_2_indicate, Menu_2_page))

Menu_2.place(x=10, y=150)

Menu_2_indicate = tk.Label(options_frame, text=" ", bg="#c3c3c3")
Menu_2_indicate.place(x=3, y=150, width=5, height=40)

Menu_3 = tk.Button(options_frame, text='Menu 3', font=('Bold', 15),
                     fg='#158aff', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(Menu_3_indicate, Menu_3_page))

Menu_3.place(x=10, y=200)

Menu_3_indicate = tk.Label(options_frame, text=" ", bg="#c3c3c3")
Menu_3_indicate.place(x=3, y=200, width=5, height=40)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=800)

main_frame = tk.Frame(root, highlightbackground="black",
                      highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=1080, width=720)

operation_var = tk.StringVar()
operation_var.set('Division')

root.mainloop()
