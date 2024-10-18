
import random
import string
def generate_password(length):
    pattern_chars = "ABCDabcd1234!@#$"
    return ''.join(random.choice(pattern_chars) for _ in range(length))
