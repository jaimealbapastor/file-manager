import shutil
import os
import sys

# os
os.getcwd()  # get current path
os.chdir("path")  # change current path

os.listdir("path")  # returns list with all file names
os.scandir("path")  # mirar en internet (mejor que listdir)
os.walk("path")  # returns tupple (root, dirs, files) for each dir in path
os.makedirs("path\dir")  # creates directory in path


os.path.exists("path")  # verifies if path exists
os.path.splitext("file.ext")  # returns ["file", ".ext"]
os.path.join("path", "file")  # returns path\file
os.path.join("path", "dir", "file")  # returns path\dir\file
os.path.isdir("path")  # checks if it's a directory
os.path.isfile("path")  # checks if it's a directory


# shutil
shutil.move("source_filepath", "destination_filepath")

# sys
sys.argv(1)  # returns parameter nb 1

sys.stdout.write("txt")  # prints txt without end="\n"
