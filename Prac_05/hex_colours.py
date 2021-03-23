"""
Print hexcode for colour
"""

NAME_TO_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74", "azure1": "#f0ffff"}

print(NAME_TO_CODE)

valid = False
while not valid:
    try:
        colour_name = str(input("Enter a colour: "))
        if colour_name != "":
            print("{0} is {1} in hex".format(colour_name, NAME_TO_CODE[colour_name]))
        else:
            valid = True
    except KeyError:
        print("Not a colour")

