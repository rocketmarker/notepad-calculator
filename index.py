class Notepad:
    def __init__(self, master):
        self.master = master
        master.title("Notepad")

        # Create Text widget
        self.text_editor = Text(master, font=("Helvetica", 16))
        self.text_editor.pack(fill=BOTH, expand=True)

        # Create Menu bar
        self.menu_bar = Menu(master)
        master.config(menu=self.menu_bar)

        # Add File menu
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=master.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Add Edit menu
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        # Add Help menu
        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="About", command=self.about)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        # Add Calculator menu
        self.calc_menu = Menu(self.menu_bar, tearoff=0)
        self.calc_menu.add_command(label="Calculate", command=self.calculate)
        self.menu_bar.add_cascade(label="Calculator", menu=self.calc_menu)

    def new_file(self):
        self.text_editor.delete(1.0, END)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                file_contents = file.read()
                self.text_editor.delete(1.0, END)
                self.text_editor.insert(1.0, file_contents)

    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, "w") as file:
                file_contents = self.text_editor.get(1.0, END)
                file.write(file_contents)

    def cut(self):
        self.text_editor.event_generate("<<Cut>>")

    def copy(self):
        self.text_editor.event_generate("<<Copy>>")

    def paste(self):
        self.text_editor.event_generate("<<Paste>>")

    def about(self):
        messagebox.showinfo("About", "This is a simple notepad application")

    def calculate(self):
        calc_window = Toplevel(self.master)
        calc_window.title("Calculator")
        calc_window.geometry("200x200")

        entry = Entry(calc_window, width=25)
        entry.pack(side=TOP, padx=10, pady=10)

        def calculate_result():
            result = eval(entry.get())
            label.config(text=f"Result: {result}")

        button = Button(calc_window, text="Calculate", command=calculate_result)
        button.pack(side=TOP, padx=10, pady=10)

        label = Label(calc_window)
        label.pack(side=TOP, padx=10, pady=10)
