# reMarkableProjects

Automate organisation of reMarkable2 files since these are deleted after 3 months.
Goals:
- Checks if new file exists and saves it in the database.
- If a file already exists, replace it with the newest version.
- Create a trash with the older versions

## File Format

`title-chapter-subject-year.ext`

Required fields: title, year, subject (if chapter exists)  
Other sub-formats:
- `title-year.ext`
- `title-subject-year.ext`


## Next steps
- download files from reMarkable web
- manage files directly in google drive
- delete trash files after x months

## How to use it
Type on the terminal:  
`python organizeRM.py [path of directory to organise :str] [isolate non formated files :bool (optional)]`