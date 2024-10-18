
import random
import string
def generate_password(length):
    return ''.join(random.choice(string.digits) for _ in range(length))

