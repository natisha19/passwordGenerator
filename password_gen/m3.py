
import random
import string
def generate_password(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))        

