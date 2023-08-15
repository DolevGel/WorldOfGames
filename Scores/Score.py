SCORES_FILE_NAME = "Scores/Scores.txt"  # Path to the Scores.txt file
POINTS_OF_WINNING = 0


def add_score(difficulty):
    try:
        with open(SCORES_FILE_NAME, "r") as file:
            current_score = int(file.read())
    except FileNotFoundError:
        current_score = 0

    new_score = current_score + calculate_points(difficulty)

    with open(SCORES_FILE_NAME, "w") as file:
        file.write(str(new_score))


def calculate_points(difficulty):
    return (difficulty * 3) + 5
