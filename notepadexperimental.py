    import tkinter as tk
    from tkinter import scrolledtext, filedialog

    class Notepad:
        def __init__(self, master):
            self.master = master
            self.master.title("Notepad")
            self.textarea = scrolledtext.ScrolledText(self.master, undo=True, font=('Lucida Console', '10'))
            self.textarea.pack(fill='both', expand=True)
            self.create_menu()

        def create_menu(self):
            menubar = tk.Menu(self.master)
            file_menu = tk.Menu(menubar, tearoff=0)
            file_menu.add_command(label="New", command=self.new_file)
            file_menu.add_command(label="Open", command=self.open_file)
            file_menu.add_command(label="Save", command=self.save_file)
            file_menu.add_separator()
            file_menu.add_command(label="Exit", command=self.master.quit)
            menubar.add_cascade(label="File", menu=file_menu)
            
            calc_menu = tk.Menu(menubar, tearoff=0)
            calc_menu.add_command(label="Calculator", command=self.calculator)
            calc_menu.add_command(label="Fraction Calculator", command=self.fraction_calculator)
            menubar.add_cascade(label="Tools", menu=calc_menu)
            
            self.master.config(menu=menubar)

        def new_file(self):
            self.textarea.delete(1.0, tk.END)

        def open_file(self):
            file_path = filedialog.askopenfilename()
            if file_path:
                with open(file_path, 'r') as file:
                    self.textarea.delete(1.0, tk.END)
                    self.textarea.insert(1.0, file.read())

        def save_file(self):
            file_path = filedialog.asksaveasfilename()
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(self.textarea.get(1.0, tk.END))
                    
        def calculator(self):
            top = tk.Toplevel(self.master)
            top.title("Calculator")
            
            input_field = tk.Entry(top, font=('Lucida Console', '10'))
            input_field.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
            input_field.bind('<Return>', lambda event: self.calculate(input_field))

            
            buttons = ['7', '8', '9', '/',
                       '4', '5', '6', '*',
                       '1', '2', '3', '-',
                       '0', '.', '=', '+']
            row = 1
            col = 0
            for button in buttons:
                if button == '=':
                    tk.Button(top, text=button, width=10, command=lambda: self.calculate(input_field)).grid(row=row, column=col, columnspan=2, padx=5, pady=5)
                else:
                    tk.Button(top, text=button, width=5, command=lambda text=button: self.append_text(input_field, text)).grid(row=row, column=col, padx=5, pady=5)
                col += 1
                if col > 3:
                    col = 0
                    row += 1
            
        def fraction_calculator(self):
            top = tk.Toplevel(self.master)
            top.title("Fraction Calculator")
        
            def gcd(a, b):
                if b == 0:
                    return a
                return gcd(b, a % b)
        
            def add_fractions(frac1, frac2):
                lcm = (frac1[1] * frac2[1]) // gcd(frac1[1], frac2[1])
                num = frac1[0] * (lcm // frac1[1]) + frac2[0] * (lcm // frac2[1])
                return (num // gcd(num, lcm), lcm // gcd(num, lcm))
        
            def subtract_fractions(frac1, frac2):
                lcm = (frac1[1] * frac2[1]) // gcd(frac1[1], frac2[1])
                num = frac1[0] * (lcm // frac1[1]) - frac2[0] * (lcm // frac2[1])
                return (num // gcd(num, lcm), lcm // gcd(num, lcm))
        
            def multiply_fractions(frac1, frac2):
                num = frac1[0] * frac2[0]
                denom = frac1[1] * frac2[1]
                return (num // gcd(num, denom), denom // gcd(num, denom))
        
            def divide_fractions(frac1, frac2):
                num = frac1[0] * frac2[1]
                denom = frac1[1] * frac2[0]
                return (num // gcd(num, denom), denom // gcd(num, denom))
        
            def simplify_fraction(frac):
                gcd_frac = gcd(frac[0], frac[1])
                return (frac[0] // gcd_frac, frac[1] // gcd_frac)
        
            def calculate_fractions():
                frac1_str = frac1_entry.get()
                frac2_str = frac2_entry.get()
        
                try:
                    frac1 = tuple(map(int, frac1_str.split('/')))
                    frac2 = tuple(map(int, frac2_str.split('/')))
                except:
                    result_label.config(text="Error: Invalid fractions")
                    return
        
                operation = operation_var.get()
                if operation == "+":
                    result = add_fractions(frac1, frac2)
                elif operation == "-":
                    result = subtract_fractions(frac1, frac2)
                elif operation == "*":
                    result = multiply_fractions(frac1, frac2)
                elif operation == "/":
                    if frac2[0] == 0:
                        result_label.config(text="Error: Division by zero")
                        return
                    result = divide_fractions(frac1, frac2)
                else:
                    result_label.config(text="Error: Invalid operation")
                    return
        
                result = simplify_fraction(result)
                result_label.config(text=f"{result[0]}/{result[1]}")
        
            frac1_label = tk.Label(top, text="Fraction 1:")
            frac1_label.grid(row=0, column=0, padx=5, pady=5)
        
            frac1_entry = tk.Entry(top, font=('Lucida Console', '10'))
            frac1_entry.grid(row=0, column=1, padx=5, pady=5)
        
            frac2_label = tk.Label(top, text="Fraction 2:")
            frac2_label = tk.Label(frac_frame, text='Denominator 2:')
            frac2_label.grid(row=1, column=2)

            
        def append_text(self, input_field, text):
            input_field.insert(tk.END, text)
        
        def calculate(self, input_field):
            try:
                result = eval(input_field.get())
                input_field.delete(0, tk.END)
                input_field.insert(0, result)
            except:
                input_field.delete(0, tk.END)
                input_field.insert(0, "Error")

    if __name__ == '__main__':
        root = tk.Tk()
        app = Notepad(root)
        root.mainloop()
