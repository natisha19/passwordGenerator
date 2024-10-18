
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import string
import random

additional_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?'
def generate_password():
        user_input = simpledialog.askstring("Password Generator", "Enter characters to be included in your password (with space): ").split()
        if not user_input:
            return  # User canceled input
        user_characters = ''.join(set(user_input))
        
     # Ensuring at least one character from each category is included in the password
        uppercase_char = random.choice(string.ascii_uppercase)
        lowercase_char = random.choice(string.ascii_lowercase)
        digit_char = random.choice(string.digits)
        additional_char = random.choice(additional_chars)

        all_chars = user_characters + uppercase_char + lowercase_char + digit_char + additional_char

        return all_chars

