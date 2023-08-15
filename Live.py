from Games.CurrencyRouletteGame import play_currency_roulette
from Games.GuessGame import play_guess_game
from Games.MemoryGame import play_memory_game
from Scores.Score import add_score


def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play."


def load_game():
    print('''Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
    ''')

    while True:
        game = input("Enter the game number (1-3): ")
        if game.isdigit() and game in ["1", "2", "3"]:
            break
        print("Please enter a number between 1 and 3.")

    while True:
        difficulty = input("Please choose game difficulty from 1 to 5: ")
        if difficulty.isdigit() and 1 <= int(difficulty) <= 5:
            break
        print("Please enter a number between 1 and 5.")

    if game == "1":
        memory_game_result = play_memory_game(int(difficulty))
        if memory_game_result:
            print("You won!")
            add_score(int(difficulty))
        else:
            print("You lost.")
    elif game == "2":
        guess_game_result = play_guess_game(int(difficulty))
        if guess_game_result:
            print("You won!")
            add_score(int(difficulty))
        else:
            print("You lost.")
    elif game == "3":
        currency_game_result = play_currency_roulette(int(difficulty))
        if currency_game_result:
            print("You won!")
            add_score(int(difficulty))
        else:
            print("You lost.")
    while True:
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y":
            print("Let's play again! ")
            load_game()
        elif play_again == "n":
            print("Hope you had fun! See you next time :)")
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'. ")

# from Games.GuessGame import play_guess_game
# from Games.MemoryGame import play_memory_game
# from Games.CurrencyRouletteGame import play_currency_roulette
# from Scores.Score import add_score
#
#
# def welcome(name):
#     return f'Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play'
#
#
# def load_game():
#     print('''
#     Please choose a game to play:
#     1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
#     2. Guess Game - guess a number and see if you chose like the computer
#     3. Currency Roulette - try and guess the value of a random amount of USD in ILS
#     ''')
#
#     while True:
#         game_choice = input("Enter the number of the game you choose (1-3), or 'q' to quit: ")
#
#         if game_choice.lower() == 'q':
#             return None, None
#
#         if not game_choice.isdigit() or int(game_choice) not in range(1, 4):
#             print("Invalid input. Please choose a valid game number.")
#             continue
#
#         difficulty_level = input("Please choose game difficulty from 1 to 5: ")
#
#         if not difficulty_level.isdigit() or int(difficulty_level) not in range(1, 6):
#             print("Invalid input. Please choose a valid difficulty level.")
#             continue
#
#         game_choice = int(game_choice)
#         difficulty_level = int(difficulty_level)
#
#         if game_choice == 1:
#             memory_game_result = play_memory_game(difficulty_level)
#             if memory_game_result:
#                 print("You won!")
#                 add_score(difficulty_level)
#             else:
#                 print("You lost.")
#
#         elif game_choice == 2:
#             guess_game_result = play_guess_game(difficulty_level)
#             if guess_game_result:
#                 print("You won!")
#                 add_score(difficulty_level)
#             else:
#                 print("You lost.")
#
#         elif game_choice == 3:
#             currency_roulette_game_result = play_currency_roulette(difficulty_level)
#             if currency_roulette_game_result:
#                 print("You won!")
#                 add_score(difficulty_level)
#             else:
#                 print("You lost.")
#
#         else:
#             print("Invalid game choice. Please choose a valid game number.")
#             continue
#
#         break
#
#         return game_choice, difficulty_level
#
#     # return int(game_choice), int(difficulty_level)
#
#
#
#     # def play_loop():
#     #     name = input("Enter your name: ")
#     #     print(welcome(name))
#     #
#     #     while True:
#     #         game_choice, difficulty_level = load_game()
#     #
#     #         if game_choice is None:
#     #             break
#     #
#     # while True:
#     #     play_loop()
#     #     play_again = input("Do you want to play again? (y/n): ")
#     #     if play_again.lower() != 'y':
#     #         break
