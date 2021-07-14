import pathlib


some_file = "vapix.py"
some_path =  pathlib.Path(some_file)
some_path.write_text("Hey")  # Write to file (safe)
some_path.unlink()  # Delete file

# Check that file exists and print full file path.
print(f"It is {some_path.exists()} that the file {some_path.absolute()} exists.")
print()

folder_path = pathlib.Path("./shorts")
verb = "is"
if not folder_path.is_dir():
   verb += " not"
# Printing it according to the OS, getting absolute path and removing symlinks.
print(f"{folder_path.resolve()} {verb} a directory.")
print()
# Adding path
print(folder_path / "A_new_file")

third_file = pathlib.Path(".handling_files").absolute()
# Only return ending of file
print(third_file.name)
# Print a list containing each parent folder
print([part for part in third_file.parents])
