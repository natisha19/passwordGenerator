import os

# Specify the name of the new directory
new_directory = "password_gen"

# Create a new directory
#os.mkdir(new_directory)  #was used to dreate a new directory password_gen

# Change the current working directory to the newly created directory
os.chdir(new_directory)  #Changing the working directory
print(os.getcwd())
print(os.listdir())

#writing into the modules

module1 = """
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

"""

module2= """
import random
import string
def generate_password(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))        

"""


module3= """
import random
import string
def generate_password(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))        

"""


module4= """
import random
import string
def generate_password(length):
    return ''.join(random.choice(string.digits) for _ in range(length))

"""

module5= """
import random
def generate_password():
    word_list = ["apple", "banana", "orange", "grape", "kiwi","peach","base"]
    return ''.join(random.choice(word_list) for _ in range(random.randint(2, 4)))
"""

module6= """
import random
import string
def generate_password(length):
    pattern_chars = "ABCDabcd1234!@#$"
    return ''.join(random.choice(pattern_chars) for _ in range(length))
"""

module7= """
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

"""

module8= """
import string
import random
special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?'
def generate_password():
   a=random.choice(string.ascii_lowercase)+random.choice(string.ascii_uppercase)+random.choice(special_chars)+random.choice(string.digits)
   return(a+a)
"""

module9= """
import string
from tkinter import simpledialog, messagebox
from password_gen import m5, m6, m7, m9

def assess_user_input_password_strength(password):
    length_score = min(len(password) // 3, 4)
    case_score = 2 if any(c.islower() for c in password) and any(c.isupper() for c in password) else 0
    digit_score = 2 if any(c.isdigit() for c in password) else 0
    special_char_score = 3 if any(c in string.punctuation for c in password) else 0

    total_score = length_score + case_score + digit_score + special_char_score

    if total_score >= 7:
        return "Strong"
    elif total_score >= 4:
        return "Moderate"
    else:
        return "Weak"

def suggest_strong_passwords(original_password):
    suggestions = [
        m6.generate_password(),
        m9.generate_password(),
        m5.generate_password(6),
        m7.generate_password(12)
    ]
    
    pp= '  ,  '.join(suggestions)
    sugg_message = (f"Your password {original_password} is not strong.Here are a few suggestions:" + f"{pp}")
    return sugg_message

def assess_and_suggest_password():
    user_input_password = simpledialog.askstring("User Input", "Enter your password:")
    password=user_input_password
    if not user_input_password:
        return  # User canceled input

    strength_result = assess_user_input_password_strength(password)

    if strength_result == "Weak":
        suggestion_message = suggest_strong_passwords(user_input_password)
        messagebox.showinfo("Weak Password", suggestion_message )
    elif strength_result == "Moderate":
        suggestion_message = suggest_strong_passwords(user_input_password)
        messagebox.showinfo("Moderate Password", suggestion_message)
    else:
        messagebox.showinfo("Password Strength", f"The strength of the password is: {strength_result}")
    return(password)
 
""" 
#creating modules as Python files 

with open("m1.py", "w") as file:
    file.write(module1)
with open("m2.py", "w") as file:
    file.write(module2)
with open("m3.py", "w") as file:
    file.write(module3)
with open("m4.py", "w") as file:
    file.write(module4)
with open("m5.py", "w") as file:
    file.write(module5)
with open("m6.py", "w") as file:
    file.write(module6)
with open("m7.py", "w") as file:
    file.write(module7)
with open("m8.py", "w") as file:
    file.write(module8)
with open("m9.py", "w") as file:
    file.write(module9)




