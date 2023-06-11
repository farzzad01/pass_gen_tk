import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.settings = {
            'lower': True,
            'upper': True,
            'number': True,
            'symbol': True,
            'space': False,
            'length': 8
        }
        self.init_ui()

    def init_ui(self):
        self.root.title("Password Generator")

        # Create label and entry for password length
        length_label = tk.Label(self.root, text=f"Password Length (default is {self.settings['length']}):")
        length_label.pack()
        self.length_entry = tk.Entry(self.root)
        self.length_entry.pack()

        # Create checkbuttons for each option
        self.lower_var = tk.IntVar(value=1)
        lower_check = tk.Checkbutton(self.root, text="Include lowercase?", variable=self.lower_var)
        lower_check.pack()

        self.upper_var = tk.IntVar(value=1)
        upper_check = tk.Checkbutton(self.root, text="Include uppercase?", variable=self.upper_var)
        upper_check.pack()

        self.number_var = tk.IntVar(value=1)
        number_check = tk.Checkbutton(self.root, text="Include numbers?", variable=self.number_var)
        number_check.pack()

        self.symbol_var = tk.IntVar(value=1)
        symbol_check = tk.Checkbutton(self.root, text="Include symbols?", variable=self.symbol_var)
        symbol_check.pack()

        self.space_var = tk.IntVar(value=0)
        space_check = tk.Checkbutton(self.root, text="Include spaces?", variable=self.space_var)
        space_check.pack()

        # Create generate button
        generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        generate_button.pack()

    def generate_password(self):
        # Get user inputs
        length = self.length_entry.get()
        self.settings['length'] = int(length) if length.isdigit() else self.settings['length']
        self.settings['lower'] = self.lower_var.get() == 1
        self.settings['upper'] = self.upper_var.get() == 1
        self.settings['number'] = self.number_var.get() == 1
        





