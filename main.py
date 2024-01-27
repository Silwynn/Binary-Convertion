import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Binary Conversion")
root.geometry('550x550')


def home_page():
    home_frame = tk.Frame(main_frame)
    home_frame.pack(pady=20)
    
    lb = tk.Label(home_frame, text='BINARY CONVERSION\n\n', font=('Bold', 30))
    lb.pack()
    
    home_frame.pack(pady=20)
    
def Menu_1_page():
    Menu_1_frame = tk.Frame(main_frame)
    
    lb = tk.Label(Menu_1_frame, text='Main Menu\n\n', font=('Bold', 30))
    lb.pack()
    
    Menu_1_frame.pack(pady=20)

def Menu_2_page():
    Menu_2_frame = tk.Frame(main_frame)
    
    lb = tk.Label(Menu_2_frame, text='Binary Conversion\n\n', font=('Bold', 30))
    lb.pack()
    
    Menu_2_frame.pack(pady=20)
    

    
def Menu_3_page():
    Menu_3_frame = tk.Frame(main_frame)
    
    lb = tk.Label(Menu_3_frame, text='Conversion System\n\n', font=('Bold', 30))
    lb.pack()
    
    Menu_3_frame.pack(pady=20)
 

    
def hide_indicators():
    home_indicate.config(bg='#c3c3c3')
    Menu_1_indicate.config(bg='#c3c3c3')
    Menu_2_indicate.config(bg='#c3c3c3')
    Menu_3_indicate.config(bg='#c3c3c3')
    
def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()
        

def indicate(lb, page):
    hide_indicators()  # Call the hide_indicators function
    lb.config(bg='#158aff')
    delete_pages()
    page()


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
options_frame.configure(width=100, height=400)

main_frame = tk.Frame(root, highlightbackground="black",
                      highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=400, width=500)



root.mainloop()
