# reMarkableProjects

Automate organisation of reMarkable2 files since these are deleted after 3 months.
Goals:
- Download files from reMarkable web
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
- manage files directly in google drive
- delete trash files after x months