from string import ascii_letters, digits
from random import choice


def random_string(length=5, prefix="Test_file", type="txt"):
    rand = ''.join(choice(ascii_letters + digits) for _ in range(length))
    return "{}_{}.{}".format(prefix, rand, type)