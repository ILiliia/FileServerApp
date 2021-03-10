import argparse
import os
from file_service import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_dir", action="store", default=None, required=True)
    options, args = parser.parse_known_args()

    os.environ['FILE_DIR_PATH'] = options.file_dir
