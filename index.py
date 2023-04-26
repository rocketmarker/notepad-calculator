import tkinter as tk
from tkinter import messagebox, filedialog
import requests
import json

class Notepad:
    def __init__(self, master):
        print("Initializing Notepad...")
        self.master = master
        self.master.title("Notepad")
        
        self.create_widgets()

    def create_widgets(self):
        # Create the text editor widget
        self.text_editor = tk.Text(self.master, font=("Helvetica", 12), undo=True)
        self.text_editor.pack(expand=True, fill="both")
        
        # Create the menu bar
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)
        
        # Create the File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_application)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        
        # Create the Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.edit_menu.add_command(label="Undo", command=self.text_editor.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_editor.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.edit_menu.add_command(label="Select All", command=self.select_all_text)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        
        # Create the Tools menu
        self.tools_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.tools_menu.add_command(label="Calculator", command=self.open_calculator)
        self.menu_bar.add_cascade(label="Tools", menu=self.tools_menu)

    # File menu functions
    def new_file(self):
        self.text_editor.delete(1.0, "end")
        
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                self.text_editor.delete(1.0, "end")
                self.text_editor.insert("end", file.read())

    def save_file(self):
        if not hasattr(self, "file_path"):
            self.save_file_as()
        else:
            with open(self.file_path, "w") as file:
                file.write(self.text_editor.get(1.0, "end"))

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            self.file_path = file_path
            self.save_file()

    def exit_application(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.master.destroy()

    # Edit menu functions
    def cut_text(self):
        self.text_editor.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_editor.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_editor.event_generate("<<Paste>>")
