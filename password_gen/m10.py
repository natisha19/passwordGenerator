
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
 
