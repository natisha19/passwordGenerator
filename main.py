import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from password_gen import m1, m2, m3, m4, m5, m6, m7, m8, m9
from strength_assessment import assess_password_strength
from history import PasswordHistory
#from m11 import assess_user_input_password_strength

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.password_var = tk.StringVar()
        self.strength_var = tk.StringVar()
        self.selected_method = tk.StringVar(value="m1")
        self.password_history = PasswordHistory()

        self.create_widgets()

    def create_widgets(self):
        # Password Entry
        password_entry_label = ttk.Label(self.root, text="Generated Password:")
        password_entry_label.grid(row=0, column=0, padx=10, pady=5, sticky="W")

        password_entry = ttk.Entry(self.root, textvariable=self.password_var, state="readonly", font=("Courier", 12))
        password_entry.grid(row=0, column=1, padx=10, pady=5, sticky="W")

        # Method Selection Dropdown
        method_label = ttk.Label(self.root, text="Password Generation Method:")
        method_label.grid(row=1, column=0, padx=16, pady=10, sticky="W")

        methods = ["User Input", "Uppercase", "Lowercase", "Digits", "Worded", "Random", "Mnemonic", "Pattern Based", "User's Password"]
        method_dropdown = ttk.Combobox(self.root, values=methods, textvariable=self.selected_method, state="readonly")
        method_dropdown.grid(row=1, column=1, padx=16, pady=10, sticky="W")

        # Generate Button
        generate_button = ttk.Button(self.root, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Strength Label
        strength_label = ttk.Label(self.root, text="Password Strength:")
        strength_label.grid(row=3, column=0, padx=16, pady=10, sticky="W")

        strength_entry = ttk.Entry(self.root, textvariable=self.strength_var, state="readonly", font=("Arial", 12))
        strength_entry.grid(row=3, column=1, padx=10, pady=5, sticky="W")

        # History Button
        history_button = ttk.Button(self.root, text="View History", command=self.display_history)
        history_button.grid(row=4, column=0, columnspan=2, pady=10)

    def generate_password(self):
        method = self.selected_method.get()

        if method == "User Input":
            generated_password = m1.generate_password()
        elif method == "Uppercase":
            generated_password = m2.generate_password(8)
        elif method == "Lowercase":
            generated_password = m3.generate_password(8)  
# Generating a single lowercase letter
        elif method == "Digits":
            generated_password = m4.generate_password(6)  
# Generating a single digit
        '''elif method == "Special Character":
            generated_password = m5.generate_password()'''  
# Generating a single special character
        elif method == "Worded":
            generated_password = m5.generate_password()
        elif method == "Custom Length":
            generated_password = m6.generate_password(8)  
# You can customize the length as needed
        elif method == "Mnemonic":
            generated_password = m7.mnemonic()
        elif method == "Pattern Based":
            generated_password = m8.generate_password()  
        elif method == "User's Password":
            generated_password = m9.assess_and_suggest_password()

        self.password_var.set(generated_password)

        strength_result = assess_password_strength(generated_password)
        self.strength_var.set(strength_result)

        self.password_history.add_to_history(generated_password)

        if strength_result == "Weak" and method in {"m1", "m2", "m3", "m4"}:
            self.suggest_strong_passwords(generated_password)

    def suggest_strong_passwords(self, original_password):
        suggestions = [
            m1.generate_password_from_user_input(original_password),
            m7.generate_password(),
            m6.generate_password(),
            m9.generate_password()
        ]
        suggestion_message = f"Your password '{original_password}' is weak. Here are a few suggestions:\n" + "\n".join(suggestions)
        messagebox.showinfo("Weak Password", suggestion_message)
     
    def display_history(self):
        self.password_history.display_history()



if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
