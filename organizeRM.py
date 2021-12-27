import os
import shutil
from sys import argv


class Category:
    general = "1~General"
    nonformated = "2~Non_Formated"
    duplicated = "3~Bin"

# TODO convertir a clase para atributos path
# TODO change shutil.move() to os.rename()


def organize_files(path: str, exclude_no_formated=False):
    r"""Organizes the files into a specific format. Check README for more.

    Args:
        path (str): path of the main directory to organise
        exclude_no_formated (bool, optional): the non formated file names can whether be moved into a non formated directory or left where they are. Defaults to False.
    """
    if not os.path.exists(path):
        print(f"ERROR. Not found {path} or not exists.")
        return

    nb_files = 0

    for root, dirs, files in os.walk(path):
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
                            move_to_duplicated(file2_path, path)
                            move(file_path, correct_root)
                        else:
                            move_to_duplicated(file_path, path)
                    else:
                        move(file_path, correct_root)

                    # ---------------------
                    nb_files += 1
                    print(f"\rFiles moved: {nb_files}", flush=True, end='')


def is_correctly_rooted(name: str, root: str, path: str) -> bool:
    r"""Checks if the file is correctly located according to the name. Check README for formatting style.

    Args:
        name (str): name of the file. EX: name of \User\Desktop\example.txt is example.txt
        root (str): path of the parent directory.
        path (str): path of the main directory to organise
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
        name (str): name of the file. EX: name of \User\Desktop\example.txt is example.txt
        path (str): path of the main directory to organise
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
    r"""Choose the newest file

    Args:
        file_path (str): path of the 1st file
        file2_path (str): path of the 2nd file

    Returns:
        str: the path of the newest file 
    """
    if os.path.getmtime(file_path) > os.path.getmtime(file2_path):
        return file_path
    return file2_path


def move(file_path: str, root: str):
    r"""Moves the file to a directory after checking if it exists. If not the directory/ies is/are created

    Args:
        file_path (str): the path of the file to move
        root (str): path of the directory where to move the file
    """
    if not os.path.isdir(root):
        os.makedirs(root)
    shutil.move(file_path, root)


def move_to_duplicated(file_path: str, path: str):
    r"""Moves the file to the duplicated directory and changes the name if it's already duplicated

    Args:
        file_path (str): path of the file
        path (str): path (str): path of the main directory to organise
    """
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


def remove_empty_folders(path_abs):
    walk = list(os.walk(path_abs))
    for path, _, _ in walk[::-1]:
        if len(os.listdir(path)) == 0:
            os.rmdir(path)


if __name__ == "__main__":
    try:
        abs_path = os.getcwd()
        exclude_non_formated = False

        if len(argv) == 2:
            abs_path = argv[1]
        elif len(argv) > 2:
            abs_path = argv[1]
            exclude_non_formated = argv[2]

        organize_files(abs_path, exclude_non_formated)
        remove_empty_folders(abs_path)
    except Exception as e:
        print(f"There was an error: {str(e)}")
