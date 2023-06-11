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

        

        
   
        





