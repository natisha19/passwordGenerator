#PASSWORD GENERATOR - STRENGTH ASSESSMENT
#This module displays the strength of the passwords generated

import string

def assess_password_strength(password):
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
