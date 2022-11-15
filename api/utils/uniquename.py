from models import User
import random
import string


def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if User.slug.filter(code=code).count() == 0:
            break
    return code
