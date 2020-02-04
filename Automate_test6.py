# Walk a directory tree and archive just files with certain extensions, such as .txt or .py, and nothing else.

import zipfile, os

os.chdir("/Users/ramteechua/Desktop/Desktop-Files/test")
# Put absolute path here.
directory = "/Users/ramteechua/Desktop/Desktop-Files/test/hello-world-fun-folder"

zip_file_name = os.path.basename(directory) + ".zip"
example_zip = zipfile.ZipFile(zip_file_name, "w")

for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        # Adds the file into the zip if it ends with the text inputted.
        if filename.endswith(".py") or filename.endswith(".txt"):
            example_zip.write(os.path.join(dirpath, filename), arcname=filename)

example_zip.close()
print("Done.")

