from os import walk, path, rename, getcwd
from sys import argv
from PIL import Image
from shutil import rmtree

#### PARAMETERS ####
spliter = '_'
words_to_ignore = ["", "td", "cours", "feuilles"]
mandatory_end = "PeiP2"


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def relative_root(root: str, abs_path: str) -> str:
    """The relative root is the root of the file relative to the folder passed as argument

    Args:
        root (str): Absolute path of the file
        path (str): Absolute path of the folder passed as argument

    Returns:
        str: the relative root of the file
    """
    if abs_path in root:
        return root[len(abs_path):]


def correct_name_end(relative_root: str) -> str:
    """The ending component of the name refering to its position in the folder

    Args:
        relative_root (str): relative root of the file

    Returns:
        str: the correct ending component of the name
    """
    parts = relative_root.split("\\")
    nb_ignored = 0
    for i in range(len(parts)):
        i -= nb_ignored
        if parts[i].lower() in words_to_ignore:
            parts.pop(i)
            nb_ignored += 1
    parts.reverse()
    parts.append(mandatory_end)
    return spliter.join(parts)


def correct_name(relative_root: str, new_name: str) -> str:
    """The correct name is composed by the filename and the ending component refering to its position in the folder

    Args:
        relative_root (str): path of the file relative to the folder
        new_name (str): filename

    Returns:
        str: the correct name of a file in a folder
    """
    return new_name + spliter + correct_name_end(relative_root)


def ask_for_name(relative_root: str, file: str) -> str:
    """Asks the user to input the correct filenames

    Args:
        root (str): path of the file relative to the folder
    Returns:
        str: the correct name of the file
    """
    name, ext = path.splitext(file)
    return correct_name(relative_root, input(
        f"{relative_root}\\{bcolors.FAIL}{name}{bcolors.ENDC}{ext}\t--> {bcolors.OKGREEN}"))+ext


try:
    abs_path = getcwd()
    combine_files = False
    if len(argv) <= 2:
        abs_path = argv[1]
    if len(argv) == 3:
        combine_files = argv[2]

    if not path.exists(abs_path):
        print(f"ERROR. Not found {abs_path} or not exists.")
    else:
        nb_pages = 0
        nb_combined = 0

        for root, dirs, files in walk(abs_path):

            if len(files) and " - page " in files[0] and files[0][-4:] == ".png":
                #### Combine to pdf ####

                image_list = [None]*len(files)
                for file in files:
                    name, ext = path.splitext(file)
                    image = Image.open(path.join(root, file)).convert('RGB')

                    page_nb = ''
                    for i in range(2, 4):
                        if name[-i] == ' ':
                            page_nb = int(name[(-i+1):])
                            break
                    image_list[page_nb-1] = image

                    nb_pages += 1

                    print(
                        f"\rPages combined: {nb_pages}\tNew PDFs: {nb_combined}", flush=True, end='')

                if len(image_list) == 1:
                    image_list[0].save(root+".pdf")

                elif len(image_list) > 1:
                    image_list[0].save(root+".pdf", save_all=True,
                                       append_images=image_list[1:])

                nb_combined += 1
                #### end ####

                if len(dirs) == 0:
                    rmtree(root, ignore_errors=True)

        nb_files = 0
        non_formated_files = []

        for root, dirs, files in walk(abs_path):
            for file in files:
                nb_files += 1
                name = path.splitext(file)[0]
                name_end = correct_name_end(relative_root(root, abs_path))
                if len(name) < len(name_end) or name_end != name[-len(name_end):]:
                    non_formated_files.append((file, root))

        print(f"\n{nb_files} files found.")

        if non_formated_files:
            if input(f"{len(non_formated_files)} non formated files found. Wish to rename ? (Y/n) ") == 'Y':
                print('')
                i = 0

                for file, root in non_formated_files:

                    i += 1
                    print(f"{i}/{len(non_formated_files)}", end='\t')

                    new_name = ask_for_name(
                        relative_root(root, abs_path), file)
                    print(bcolors.ENDC, end='')
                    rename(path.join(root, file), path.join(root, new_name))
                    # print(f"\rFiles moved: {nb_files}", flush=True, end='')
        else:
            print(f"{bcolors.OKGREEN}All files formatted.{bcolors.ENDC}")


except Exception as e:
    print(f"There was an error: {str(e)}")
