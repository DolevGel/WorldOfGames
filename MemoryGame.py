import random
import time
from Utils import clear_screen


def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]


def get_list_from_user(difficulty):
    user_list = []
    for _ in range(difficulty):
        while True:
            num = int(input("Enter a number between 1 and 101: "))

            if 1 <= num <= 101:
                user_list.append(num)
                break
            else:
                print("Invalid input. Please enter a number within the range.")
    return user_list


def is_list_equal(list1, list2):
    return list1 == list2


def play_memory_game(difficulty):
    sequence = generate_sequence(difficulty)
    print("Memorize the numbers:")
    print(sequence)
    time.sleep(0.7)
    clear_screen()
    print("Now enter the numbers you remember:")
    user_list = get_list_from_user(difficulty)
    return is_list_equal(sequence, user_list)
