import sys
import os
from time import sleep
import organiserCours

path = os.getcwd()


if __name__ == "__main__":
    try:
        organiserCours.organize_files(path, True)
    except Exception as e:
        print(f"There was an error: {str(e)}")
