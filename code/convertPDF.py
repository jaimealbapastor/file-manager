from PIL import Image
import os
from sys import argv
from shutil import rmtree


if __name__ == "__main__":
    try:
        if len(argv) == 1:
            path = os.getcwd()
        elif len(argv) == 2:
            path = argv[1]

        nb_files = 0
        nb_pages = 0

        for root, dirs, files in os.walk(path):
            if len(files) and " - page " in files[0] and files[0][-4:] == ".png":
                image_list = [None]*len(files)
                for file in files:
                    name, ext = os.path.splitext(file)
                    image = Image.open(os.path.join(root, file)).convert('RGB')

                    page_nb = ''
                    for i in range(2, 4):
                        if name[-i] == ' ':
                            page_nb = int(name[(-i+1):])
                            break
                    image_list[page_nb-1] = image
                    nb_pages += 1
                    print(
                        f"\rPages combined: {nb_pages}\tNew PDFs: {nb_files}", flush=True, end='')

                if len(image_list) == 1:
                    image_list[0].save(root+".pdf")

                elif len(image_list) > 1:
                    image_list[0].save(root+".pdf", save_all=True,
                                       append_images=image_list[1:])

                nb_files += 1
                if len(dirs) == 0:
                    rmtree(root, ignore_errors=True)

    except Exception as e:
        print(f"There was an error: {str(e)}")
