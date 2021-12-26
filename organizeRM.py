import os
import shutil
import sys


def organize_files(path: str, exclude_no_formated=False):
    """Organize the files"""
    if not os.path.exists(path):
        print(f"ERROR. Not found {path} or not exists.")
        return

    nb_files = 0

    for root, dirs, files in os.walk(path):
        nb_files += len(files)

        print(f"\rFiles found: {nb_files}", flush=True, end='')

        for file in files:
            if not is_correctly_rooted(file, root):
                if correct_root_of(file) != "#no-formated" or exclude_no_formated:
                    move(os.path.join(root, file),
                         correct_root_of(os.path.join(root, file)))


def is_correctly_rooted(name: str, root: str) -> bool:
    r"""Checks if the file is correctly located according to the name. Check README for formatting style.

    Args:
        name (str): name of the file. EX: name of \User\Desktop\example.txt is example.txt
        root (str): absolute path of the parent directory.
    """

    # name = title-chapter-subject-year.ext
    # correct_root = parent_path\subject\year-chapter

    correct_root = correct_root_of(os.path.join(root, name))
    relative_root = root[-len(correct_root):]

    return correct_root == relative_root


def correct_root_of(file_path: str) -> str:
    r"""Returns the correct root according to the file name

    Args:
        file_name (str): name of the file. EX: name of \User\Desktop\example.txt is example.txt
    """
    name = os.path.splitext(os.path.basename(file_path))[0].split("-")
    root = os.path.dirname(file_path)

    if len(name) == 4:
        # title-chapter-subject-year.ext -> \subject\year-chapter
        return os.path.join(root, name[2], name[3]+"-"+name[1])
    elif len(name) == 3:
        # title-subject-year.ext -> \subject
        return os.path.join(root, name[1])
    elif len(name) == 2:
        # title-year.ext -> \general-year
        return os.path.join(root, "#General-"+name[1])

    return os.path.join(root, "#no-formated")


def newest(file_path: str, file2_path: str) -> str:
    if os.path.getmtime(file_path) < os.path.getmtime(file2_path):
        return file_path
    return file2_path


def move(file_path: str, dir_path: str):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    file2_path = os.path.join(dir_path, os.path.basename(file_path))

    if os.path.isfile(file2_path):
        if file_path == newest(file_path, file2_path):
            print(f"{file_path}\tis newest than\t{file2_path}")
        else:
            print(f"{file_path}\tis oldest than\t{file2_path}")

    # if file_path == newest(file_path, dir_path):

    # moves the file to the dir given

    shutil.move(file_path, dir_path)
