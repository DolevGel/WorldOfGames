import os

SCORES_FILE_NAME = "Scores.txt"

BAD_RETURN_CODE = -1


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
