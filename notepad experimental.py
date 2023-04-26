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
        file_menu.add_command(label="Talk to ChatGPT", command=self.talk_to_chatgpt)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        calc_menu = tk.Menu(menubar, tearoff=0)
        calc_menu.add_command(label="Calculator", command=self.calculator)
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
