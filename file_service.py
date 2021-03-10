from utils import *
import os
import time

dir = os.environ.get("FILE_DIR_PATH")
file_name = random_string()
file_path = os.path.join(dir, file_name)


def create_file(name=file_path):
    with open(name, 'w') as f:
        f.write(time.asctime())
        print("File created")


def read_file_content(_file=file_path):
    with open(_file, 'r') as f:
        print("File opened for reading")
        content = f.read()
        print(content)


def delete_file(file=file_path):
    os.remove(file)
    print("File removed")

