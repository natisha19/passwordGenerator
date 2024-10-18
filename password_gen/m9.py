
import string
import random
special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?'
def generate_password():
   a=random.choice(string.ascii_lowercase)+random.choice(string.ascii_uppercase)+random.choice(special_chars)+random.choice(string.digits)
   return(a+a)
