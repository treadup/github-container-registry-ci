"""
Computes the sha1 hash of the content of the following files
concatenated together.
1. requirements.txt
2. dependencies.dockerfile
3. scripts/build_docker_image.sh
"""
import hashlib
import sys

def read_file(filename):
    """
    Read contents of file.
    """
    with open(filename, "r") as f:
        return f.read()

def files_for_environment():
    """
    Returns a list the files that should checked
    for the given environment.
    The different environments use different files
    to build the docker images.
    The file hash should only change when one of
    these files changes.
    """
    environment = sys.argv[1]
    if environment == "local":
        return [
            "requirements.txt",
            "dependencies.dockerfile",
            "scripts/build_docker_image.sh"
        ]
    elif environment == "ci":
        return [
            "requirements.txt",
            "dependencies.dockerfile",
            "scripts/build_docker_image_ci.sh"
        ]

def read_all_files():
    """
    Read the content of all the files that should be
    checked for the given environment and returns their
    concatenated content.
    """
    files = files_for_environment()
    content = [read_file(f) for f in files]
    return "\n".join(content)

def print_hash(text):
    """
    Print the sha1 hash of the text.
    """
    print(hashlib.sha1(text.encode('utf-8')).hexdigest())

def check_usage():
    """
    Check that the usage is correct.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 filehash <environment>")
        print("where <environment> can be 'local' or 'ci'.")
        sys.exit(1)
    environment = sys.argv[1]
    if environment not in ("local", "ci"):
        print("You need to specify 'local' or 'ci' as the environment.")
        sys.exit(1)

check_usage()

text = read_all_files()
print_hash(text)
