from utils import *
import os
dir = os.environ.get("FILE_DIR_PATH")
file_name = random_string()
file_path = os.path.join(dir, file_name)


def create_file(name=file_path):
    with open(name, 'w'):
        print("File created")


def read_file_content(_file=file_path):
    with open(_file, 'r') as f:
        f.read()
        print("File opened for reading")


def delete_file(file=file_path):
    os.remove(file)
    print("File removed")

