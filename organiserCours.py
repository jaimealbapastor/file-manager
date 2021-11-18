import os
import shutil
import sys


def extract_files(path: str):
    # extracts all the files from folders
    if not os.path.exists(path):
        print(f"ERROR. Not found {path} or not exists.")
        return

    file_list = []
    dir_list = []

    for root, dirs, files in os.walk(path):
        file_list += files
        dir_list += dirs

        print(f"\rFiles found: {len(file_list)}", flush=True, end='')

        for file in files:
            move(os.path.join(root, file), "NotClassified")

        if root != path and len(dir_list) == 0:
            os.remove(root)
    print('')
    return


def move(file_path: str, dir_path: str):
    # moves the file to the dir given
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    shutil.move(file_path, dir_path)


def organize(path: str):
    # organize de files from
    return


path = "C:/Users/Jaime/Desktop/pruebaficheros"

extract_files(path)
