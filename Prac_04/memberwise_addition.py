"""
Memberwise addition extension
"""

LIST_ONE = [1, 2, 3]
LIST_TWO = [1, 2, 3, 4]


def main():
    added_list = add_memberwise(LIST_ONE, LIST_TWO)
    print(added_list)


def add_memberwise(list_one: list, list_two: list) -> list:
    #Checks how many numbers can be added before the lists go out of index
    if len(list_one) == len(list_two):
        min_length = len(list_one)
    elif len(list_one) < len(list_two):
        min_length = len(list_one)
    else:
        min_length = len(list_two)

    #Adds numbers together
    added_list = []
    for number in range(min_length):
        added_number = list_one[number] + list_two[number]
        added_list.append(added_number)

    #Adds numbers that haven't been added if list are not same length
    if len(list_one) != len(list_two):
        if len(list_one) < len(list_two):
            for number in range(min_length, len(list_two)):
                added_list.append(list_two[number])
        else:
            for number in range(min_length, len(list_one)):
                added_list.append(list_one[number])

    return added_list


main()

