"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        # print("Directory:", directory_name)
        # print("\tcontains subdirectories:", subdirectories)
        # print("\tand files:", filenames)
        # print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_word = split_word_by_capitals(filename)
            print(f"{filename} becomes {new_word}")

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def split_word_by_capitals(filename):
    """Splits a file name by lowercase and capitals"""
    slice_positions = [0]
    new_filename = []
    # Gets position of lowercase to uppercase to know where to splice word
    for number in range(len(filename)):
        if number + 1 < len(filename) and filename[number].islower() and filename[number + 1].isupper():
            slice_positions.append(number + 1)

    # Splices word into an array based off values gotten above
    for number in range(len(slice_positions)):
        if number + 1 < len(slice_positions):
            new_filename.append(filename[slice_positions[number]:slice_positions[number + 1]])
        else:
            new_filename.append(filename[slice_positions[number]:])

    # Turns array into new word
    new_word = "_".join(new_filename)
    return new_word


main()
