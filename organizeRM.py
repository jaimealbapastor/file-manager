import os
import shutil
import sys


class Category:
    general = "1~General"
    nonformated = "2~Non_Formated"
    duplicated = "3~Bin"

# TODO convertir a clase para atributos path


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
            if not is_correctly_rooted(file, root, path) and Category.duplicated not in root:
                correct_root = correct_root_of(file, path)
                if exclude_no_formated or Category.nonformated not in correct_root:

                    # --- Move & Manage Replacement ---
                    file_path = os.path.join(root, file)
                    file2_path = os.path.join(
                        correct_root, file)

                    if os.path.isfile(file2_path):
                        if file_path == newest(file_path, file2_path):
                            move_to_bin(file2_path, path)
                            move(file_path, correct_root)
                        else:
                            move_to_bin(file_path, path)
                    else:
                        move(file_path, correct_root)

                    # ---------------------


def is_correctly_rooted(name: str, root: str, path: str) -> bool:
    r"""Checks if the file is correctly located according to the name. Check README for formatting style.

    Args:
        name (str): name of the file. EX: name of \User\Desktop\example.txt is example.txt
        root (str): absolute path of the parent directory.
    """

    # name = title-chapter-subject-year.ext
    # correct_root = parent_path\subject\year-chapter

    correct_root = correct_root_of(name, path)
    relative_root = root[-len(correct_root):]

    return correct_root == relative_root


def correct_root_of(name: str, path: str) -> str:
    r"""Returns the correct root according to the file name and path.
    Can be used with absolute and relative path

    Args:
        file_name (str): name of the file. EX: name of \User\Desktop\example.txt is example.txt
    """
    name_parts = os.path.splitext(name)[0].split("-")

    if len(name_parts) == 4:
        # title-chapter-subject-year.ext -> \subject\year-chapter
        return os.path.join(path, name_parts[2], name_parts[3]+"-"+name_parts[1])
    elif len(name_parts) == 3:
        # title-subject-year.ext -> \subject
        return os.path.join(path, name_parts[1])
    elif len(name_parts) == 2:
        # title-year.ext -> \general-year
        return os.path.join(path, Category.general+name_parts[1])

    return os.path.join(path, Category.nonformated)


def newest(file_path: str, file2_path: str) -> str:
    if os.path.getmtime(file_path) > os.path.getmtime(file2_path):
        return file_path
    return file2_path


def move(file_path: str, dir_path: str):
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    shutil.move(file_path, dir_path)


def move_to_bin(file_path: str, path: str):
    bin_path = os.path.join(path, Category.duplicated)
    file_in_bin_path = os.path.join(bin_path, os.path.basename(file_path))
    if os.path.isfile(file_in_bin_path):

        path_split = os.path.splitext(file_in_bin_path)
        no_ext = path_split[0]
        ext = path_split[1]

        nb = 1

        while os.path.isfile(no_ext+f'({nb})'+ext):
            nb += 1
        new_file_path = no_ext+f'({nb})'+ext

        os.rename(file_path, new_file_path)  # also moves the file to the bin

    else:
        move(file_path, bin_path)


try:
    organize_files("C:\\Users\\Jaime\\Desktop\\test")
except Exception as e:
    print(f"There was an error: {str(e)}")
