import sys
import os
from time import sleep
import organiserCours

path = os.getcwd()

for root, dirs, files in os.walk(path):
    for file in files:
        print(f"{organiserCours.is_correctly_located(file,root)}\t{file}\t{root}")
    # print(organiserCours.is_correctly_located())

print(os.path.join("filename", "dir"))
