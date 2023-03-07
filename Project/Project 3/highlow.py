from deck import Deck


def game_info():
    print("HighLow is a simple card game.")
    print("During each turn of this game, a card is drawn from a shuffled deck of cards.")
    print("You have to predict whether the next card will be higher or lower (based on card rank alone).")
    print("Your score in the game is the number of correct predictions you make before you guess wrong.")
    print("Making a wrong prediction ends the game.\n")


def main():
    # print game information
    game_info()

    # create a deck of cards and shuffle it
    deck = Deck()
    deck.shuffle()
    nbr_guesses = 0

    current_card = deck.deal()
    print(f"The first card drawn from the deck is {current_card}")

    # TO DO: REPLACE "pass" statement below with your implementation
    while True:
        # ask the user to predict if the next card will be higher or lower
        user_input = input("Will the next card be higher (H/h) or Lower (L/l)? ")
        if user_input.lower() not in {"h", "l"}:
            print("Invalid input. Please enter 'H' or 'L' (case-insensitive).")
            continue

        # draw the next card and compare ranks
        next_card = deck.deal()
        print(f"The next card is {next_card}")
        if next_card.get_rank() == current_card.get_rank():
            print("The rank value is same as the previous card. Sorry, you lose on ties. The game is over.")
            break
        elif (user_input.lower() == "h" and next_card.get_rank() > current_card.get_rank()) \
                or (user_input.lower() == "l" and next_card.get_rank() < current_card.get_rank()):
            nbr_guesses += 1
            print("Your prediction was correct.")
        else:
            print("Your prediction was wrong. The game is over.")
            break

        # show the current card and continue playing
        current_card = next_card
        print(f"The current card is {current_card}")

    # DO NOT MODIFY CODE BELOW
    print("The game is over.")
    print(f"You made {nbr_guesses} correct predictions.")


# call main() function if this module is executed as a top-level script
if __name__ == "__main__":
    main()

#Author: Aditya Dube (G02500368)