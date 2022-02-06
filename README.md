# reMarkableProjects

Automate organisation of reMarkable2 files since these are deleted after 3 months.  
**organiseRM.py**:
- Checks if new file exists and saves it in the database.
- If a file already exists, the older version is replaced by the newer one.
- Creates a bin with the older versions.
- Creates a folder with the non formatted files (optional).
- Deletes the empty folders.  

**convertPDF.py**:
- Combines the images into pdf with the parent directory name.
- Deletes permanently the original folder with images after the pdf is created.

**formatNames**:  
- Opposite idea of *organiseRM.py*
- Files must be properly located
- Check if the files are correctly formated
- If not, through the command line, input only the name of the file.  
The end of the name will be added depending on its location.
- Mandatory elements can be added at the end.  
(see parameters at the beginning of the code)
- Specific folder names can be ignored so they don't appear in the file name.  
(see parameters at the beginning of the code)


## File Format

`title_chapter_subject_year.ext` (more subfolders can exist)

Required fields: title
Other sub-formats ideas:
- `title-year.ext`
- `title-subject-year.ext`

## How to use it
To organize your files type in the terminal:  
`python organizeRM.py [path of directory to organise :str (optional)] [isolate non formated files :bool (optional)]`  

To convert folder with images to pdf type in the terminal:  
`python convertPDF.py [path of the directory with the folders: str (optional)]`  

To format file names type in the terminal:  
`python formatNames.py [path of the directory with the folders: str (optional)] [combine png to pdf: bool (optional)]`

## Next steps
-[x] combine compressed images into pdf
-[ ] download files from reMarkable web
-[ ] manage files directly in google drive
-[ ] delete trash files after x months
-[x] rename files from folder position

