
import random
import string
def generate_special_char_password(length=8):
    special_chars = string.punctuation
    return ''.join(random.choice(special_chars) for _ in range(length))
