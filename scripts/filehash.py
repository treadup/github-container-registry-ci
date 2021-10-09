"""
Computes the sha1 hash of the content of the following files
concatenated together.
1. requirements.txt
2. dependencies.dockerfile
3. scripts/build_docker_image.sh
"""
import hashlib

def read_file(filename):
    """
    Read contents of file.
    """
    with open(filename, "r") as f:
        return f.read()

def read_all_files():
    content = [
        read_file("requirements.txt"),
        read_file("dependencies.dockerfile"),
        read_file("scripts/build_docker_image.sh")
    ]
    return "\n".join(content)

def print_hash(text):
    """
    Print the sha1 hash of the data.
    """
    print(hashlib.sha1(text.encode('utf-8')).hexdigest())

text = read_all_files()
print_hash(text)
