import os
import shutil


def main():
    """Moves files into directories based off of file type"""
    filetypes_to_directory = {}
    os.chdir("FilesToSort")
    for directory_name, subdirectories, filenames in os.walk('.'):
        # print(directory_name)
        # print(subdirectories)
        # print(filenames)

        filetypes = get_file_types(filenames)
        filetypes_to_directory = make_directories(filetypes, filetypes_to_directory)
        move_files(filenames, filetypes_to_directory)


def get_file_types(filenames):
    """Make directories based off of file types"""
    filetypes = []
    for filename in filenames:
        if filename.split(".")[1] not in filetypes:
            filetypes.append(filename.split(".")[1])
    return filetypes


def make_directories(filetypes, filetypes_to_directory):
    """Make directories based off user choice"""
    for filetype in filetypes:
        directory = input(f"What category would you like to sort {filetype} files into? ")
        filetypes_to_directory[filetype] = directory
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass
    return filetypes_to_directory


def move_files(filenames, filetypes_to_directory):
    """Move files to right directory"""
    for filename in filenames:
        shutil.move(filename, filetypes_to_directory[filename.split('.')[1]] + '/')

main()