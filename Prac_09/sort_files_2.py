import os
import shutil


def main():
    """Moves files into directories based off of file type"""
    os.chdir("FilesToSort")
    for directory_name, subdirectories, filenames in os.walk('.'):
        # print(directory_name)
        # print(subdirectories)
        # print(filenames)

        filetypes = get_file_types(filenames)
        print(filetypes)


def get_file_types(filenames):
    """Make directories based off of file types"""
    filetypes = []
    for filename in filenames:
        if filename.split(".")[1] not in filetypes:
            filetypes.append(filename.split(".")[1])
    return filetypes


main()