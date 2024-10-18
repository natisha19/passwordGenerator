#PASSWORD GENERATOR - HISTORY
#This module maintains and history of the passwords generated


import tkinter as tk
from tkinter import ttk

class PasswordHistory:
    def __init__(self):
        self.history = []

    def add_to_history(self, password):
        self.history.append(password)

    def display_history(self):
        history_window = tk.Toplevel()
        history_window.title("Password History")

        history_label = ttk.Label(history_window, text="Password History:")
        history_label.pack(padx=10, pady=5)

        history_listbox = tk.Listbox(history_window)
        history_listbox.pack(padx=10, pady=5)

        for password in self.history:
            history_listbox.insert(tk.END, password)

        history_window.mainloop()

