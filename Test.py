import sys
import os
from time import sleep
from file_organizer import directory
import organizeRM

#path = os.getcwd()

if __name__ == "__main__":
    try:
        directory_location = sys.argv[1]
        if len(sys.argv) < 3:
            organizeRM.organize_files(directory_location)
        else:
            organizeRM.organize_files(directory_location, sys.argv[2])
    except Exception as e:
        print(f"There was an error: {str(e)}")
