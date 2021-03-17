"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""

ROWS = 11
COLUMNS = 5

def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings[0:]]
        score_values.append(score_numbers)
    scores_file.close()
    column = 0
    temporary_results = [] #temporary list of each result for each subject, resets when it  goes to new subject
    full_results = [] #list of each result in order based on subjects, does not reset when going to new subject
    for i in range(len(subjects)):
        print(subjects[i], "Scores:")
        for score in range(len(score_values)):
            temporary_results.append(score_values[score][column])
        print(str(temporary_results)[1:-1])
        print("Max:", max(temporary_results))
        print("Min:", min(temporary_results))
        print("Avg:", sum(temporary_results)/len(temporary_results))
        print()
        full_results.append(temporary_results)
        temporary_results = []
        column += 1

    for row in range(ROWS):
        for column in range(COLUMNS):
            if row == 0:
                print("{0:^5} ".format(subjects[column]), end="")
            else:
                print("{0:^5} ".format(full_results[column][row - 1]), end="")
        print()


main()
