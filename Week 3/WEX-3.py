#
# Weekly Exercise #3: Decisions and Loops
# Author: Aditya Dube (G02500368)

import random

def play_game():
    name = input("Hello, what is your name? ")
    target_number = random.randint(1, 100)
    num_tries = 0

    print(f"{name}, I am thinking of a number between 1 and 100 (both included). Can you guess what it is...")

    while True:
        user_guess = int(input("Guess a number (1-100): "))
        num_tries += 1

        if user_guess == target_number:
            if num_tries > 7:
                print(f"{name}, you won in {num_tries} tries. It took you more than 7 tries, consider a different strategy in order to improve your performance")
            else:
                print(f"{name}, you won in {num_tries} tries. Congratulations!")
            play_again = input("Do you want to continue to play? (yes/no) ")
            if play_again.lower() == "yes":
                play_game()
            else:
                print("Thank you for playing this game. Bye.")
                break
        elif user_guess < target_number:
            print("Too low, try again.")
        else:
            print("Too high, try again.")

play_game()



