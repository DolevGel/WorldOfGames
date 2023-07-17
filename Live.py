from GuessGame import play_guess_game
from MemoryGame import play_memory_game
from CurrencyRouletteGame import play_currency_roulette
from Score import add_score


def welcome():
    name = str(input("Hello player please enter your name: "))
    return f'Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play'


def load_game():
    print('''
    Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
    ''')

    while True:
        game_choice = input("Enter the number of the game you choose (1-3), or 'q' to quit: ")

        if game_choice.lower() == 'q':
            return None, None

        if not game_choice.isdigit() or int(game_choice) not in range(1, 4):
            print("Invalid input. Please choose a valid game number.")
            continue

        difficulty_level = input("Please choose game difficulty from 1 to 5: ")

        if not difficulty_level.isdigit() or int(difficulty_level) not in range(1, 6):
            print("Invalid input. Please choose a valid difficulty level.")
            continue

        game_choice = int(game_choice)
        difficulty_level = int(difficulty_level)

        if game_choice == 1:
            MemoryGameResult = play_memory_game(difficulty_level)
            if MemoryGameResult:
                print("You won!")
                add_score(difficulty_level)

        elif game_choice == 2:
            GuessGameResult = play_guess_game(difficulty_level)
            if GuessGameResult:
                print("You won!")
                add_score(difficulty_level)

        elif game_choice == 3:
            CurrencyRouletteGameResult = play_currency_roulette(difficulty_level)
            if CurrencyRouletteGameResult:
                print("You won!")
                add_score(difficulty_level)

        else:
            print("Invalid game choice. Please choose a valid game number.")
            continue

        break

        return game_choice, difficulty_level

    # return int(game_choice), int(difficulty_level)

    def play_loop():
        print(welcome())

        while True:
            game_choice, difficulty_level = load_game()

            if game_choice is None:
                break

        return game_choice, difficulty_level

    while True:
        play_loop()
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break

# print(welcome())
#
# while True:
#     game_choice, difficulty_level = load_game()
#
#     if game_choice is None:
#         break
#
#     if game_choice == 1:
#         GuessGameResult = play_guess_game(difficulty_level)
#         if GuessGameResult:
#             print("You won!")
#         else:
#             print("You lost.")
#
#     elif game_choice == 2:
#         MemoryGameResult = play_memory_game(difficulty_level)
#         if MemoryGameResult:
#             print("You won!")
#         else:
#             print("You lost.")
#
#     elif game_choice == 3:
#         CurrencyRouletteGameResult = play_currency_roulette(difficulty_level)
#         if CurrencyRouletteGameResult:
#             print("You won!")
#         else:
#             print("You lost.")
