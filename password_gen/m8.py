
import random
import tkinter as tk
from tkinter import messagebox

def mnemonic():
    mnemonics = [
        "Every Good Boy Deserves Fun",
        "My Very Educated Mother Just Served Us Noodles",
        "King Philip, Come Out For Goodness' Sake",
        "Please Excuse My Dear Aunt Sally",
        "Richard Of York Gave Battle In Vain"
    ]

    # Choose a random mnemonic from the list
    selected_mnemonic = random.choice(mnemonics)

    mnemonic_password = ''.join(word[0] for word in selected_mnemonic.split())

    reference_message = f"The phrase '{selected_mnemonic}' becomes '{mnemonic_password}'."
    
    messagebox.showinfo("Mnemonic Password Reference", reference_message)

    return mnemonic_password

