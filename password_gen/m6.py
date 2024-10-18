
import random
def generate_password():
    word_list = ["apple", "banana", "orange", "grape", "kiwi","peach","base"]
    return ''.join(random.choice(word_list) for _ in range(random.randint(2, 4)))
