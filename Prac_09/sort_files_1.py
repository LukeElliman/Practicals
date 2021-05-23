import os
import shutil


def main():
    """Moves files into directories based off of file type"""
    os.chdir("FilesToSort")
    for directory_name, subdirectories, filenames in os.walk('.'):
        # print(directory_name)
        # print(subdirectories)
        # print(filenames)

        make_directories(filenames)
        move_directories(filenames)


def make_directories(filenames):
    """Make directories based off of file types"""
    for filename in filenames:
        try:
            os.mkdir(filename.split(".")[1])
        except FileExistsError:
            pass


def move_directories(filenames):
    """Move files to directories depending on filetype"""
    for filename in filenames:
        shutil.move(filename, filename.split(".")[1] + "/" )

main()