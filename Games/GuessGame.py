import random


def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {difficulty}: "))

            if 1 <= guess <= difficulty:
                return guess
            else:
                print("Invalid input. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def compare_results(secret_number, guess):
    if guess == secret_number:
        print("Congratulations! You guessed the correct number!")
        return True
    else:
        print("Oops! Your guess was incorrect.")
        return False


def play_guess_game(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    return compare_results(secret_number, guess)
