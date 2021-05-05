import os


def main():
    """Moves files into directories based off of file type"""
    os.chdir("FilesToSort")
    for directory_name, subdirectories, filenames in os.walk('.'):
        # print(directory_name)
        # print(subdirectories)
        # print(filenames)


def make_directories():
    print("Placeholder")

main()