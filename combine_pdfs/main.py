
import PyPDF2
from Interlayer import InterlayerFactory
from os import walk, path
from tkinter import filedialog

# ask for folder
folder_selected = filedialog.askdirectory()
folder_selected = folder_selected.replace('/', "\\")

int_factory = InterlayerFactory(folder_selected)
files_to_merge = []  # will be merged at last when interlayers are generated

years_to_avoid = ["2016","2017","2018","2019","2020","2022","2023"]

print("===== Looping for files =====")
for root, dirs, files in walk(folder_selected):
    print("=> Looping directory:\t"+root)
    # check if year correspond: 2021
    year_is_correct = True
    for year in years_to_avoid:
        if year in root: 
            year_is_correct = False
    if not year_is_correct: continue    
    
    interlayer_has_been_added = False

    # remove non pdf files
    print("Removing non pdf files", end='\t')
    i = 0
    while i < len(files):
        if path.splitext(files[i])[1] != ".pdf":
            files.pop(i)
            i -= 1  # TODO check if this line is really necesary, may cause problem
        i += 1
    print("done")
    # loop for pdf files only
    
    for file in files:

        if not interlayer_has_been_added:
            # interlayer creation issues are handled by Interlayer.py
            il_name = int_factory.create_interlayer(
                root, files)

            files_to_merge.append(il_name)
            interlayer_has_been_added = True

        # adding files to merge list
        print("\tAdding " + file, end='\t')
        
        filename = path.join(root, file)
        readpdf = PyPDF2.PdfReader(open(filename, 'rb'))
        
        files_to_merge.append(filename)
        if len(readpdf.pages) % 2 == 1:
            files_to_merge.append(int_factory.blank_page)
            
        print("done")

# merge files
print("===== Merging files =====")
merger = PyPDF2.PdfMerger(strict=False)
for pdf in files_to_merge:
    print("Merging "+ pdf, end='\t')
    merger.append(pdf)
    print("done")
    
merger.write(path.join(folder_selected, path.join(
    int_factory.parent_dir, "result.pdf")))
merger.close()
print("\nDONE !")