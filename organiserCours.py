import os
import shutil
import sys


def organize_files(path: str, exclude_no_formated=False):
    """Organise the files"""
    if not os.path.exists(path):
        print(f"ERROR. Not found {path} or not exists.")
        return

    nb_files = 0

    for root, dirs, files in os.walk(path):
        nb_files += len(files)

        print(f"\rFiles found: {nb_files}", flush=True, end='')

        for file in files:
            if not is_correctly_rooted(file, root):
                if correct_root_of(file)[0] != '#' or exclude_no_formated:
                    move(os.path.join(root, file),
                         os.path.join(correct_root_of(file)))

    return


def move(file_path: str, dir_path: str):
    # moves the file to the dir given
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    shutil.move(file_path, dir_path)


def is_correctly_rooted(file_name: str, file_root: str) -> bool:
    r"""Checks if the file is correctly located according to the name. Check README for formatting style.

    Args:
        file_name (str): name of the file. EX: name of \User\Desktop\example.txt is example.txt
        file_root (str): absolute path of the parent directory.
    """

    # name = title-chapter-subject-year.ext
    # correct_root = parent_path\subject\year-chapter

    correct_root = correct_root_of(file_name)
    relative_root = file_root[-len(correct_root):]

    return correct_root == relative_root


def correct_root_of(file_name: str) -> str:
    r"""Returns the correct path according to the file name

    Args:
        file_name (str): name of the file. EX: name of \User\Desktop\example.txt is example.txt
    """
    name = os.path.splitext(file_name)[0].split("-")

    if len(name) == 4:
        # title-chapter-subject-year.ext -> \subject\year-chapter
        return os.path.join(name[2], name[3]+"-"+name[1])
    elif len(name) == 3:
        return os.path.join(name[1])  # title-subject-year.ext -> \subject
    elif len(name) == 2:
        # title-year.ext -> \general-year
        return os.path.join("#General-"+name[1])

    return "#no-formated"


path = "C:/Users/Jaime/Desktop/pruebaficheros"
