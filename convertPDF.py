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

        for root, dirs, files in os.walk(path):
            image_list = []
            for file in files:
                image = Image.open(os.path.join(root, file)).convert('RGB')
                image_list.append(image)
            if len(image_list) == 1:
                image_list.save(root+".pdf")
            elif len(image_list) > 1:
                image_list[0].save(root+".pdf", save_all=True,
                                   append_images=image_list[1:])

            if len(dirs) == 0:
                rmtree(root, ignore_errors=True)

    except Exception as e:
        print(f"There was an error: {str(e)}")
