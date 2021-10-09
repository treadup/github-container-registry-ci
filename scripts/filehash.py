"""
Computes the sha1 hash of the requirements.txt file. This hash should
be used
"""
import hashlib

def read_file():
    """
    Read requirements file as binary.
    """
    with open("requirements.txt", "r") as f:
        return f.read().encode('utf-8')

def print_hash(data):
    """
    Print the sha1 hash of the data.
    """
    print(hashlib.sha1(data).hexdigest())

data = read_file()
print_hash(data)
