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

## File Format

`title-chapter-subject-year.ext`

Required fields: title, year, subject (if chapter exists)  
Other sub-formats:
- `title-year.ext`
- `title-subject-year.ext`

## How to use it
To organize your files type in the terminal:  
`python organizeRM.py [path of directory to organise :str] [isolate non formated files :bool (optional)]`  

To convert folder with images to pdf type in the terminal:  
`python convertPDF.py [path of the directory with the folders: str]`

## Next steps
- combine compressed images into pdf
- download files from reMarkable web
- manage files directly in google drive
- delete trash files after x months

