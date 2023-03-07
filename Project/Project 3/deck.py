from card import Card
from random import shuffle

class Deck(object):
    """Deck class models a standard deck of playing cards containing 52 cards."""

    def __init__(self):
        """
        Initializes a deck with an unshuffled deck of 52 cards.
        
        Instance variables:
            self._cards: a list initialized with 52 Card objects in a standard deck of cards.
        """
        self._cards = []
        for rank in range(1, 14):
            for suit in range(1, 5):
                self._cards.append(Card(rank, suit))

    def size(self):
        """Returns the size (number of cards) of the deck."""
        return len(self._cards)

    def is_empty(self):
        """Returns True if the deck is empty, False otherwise."""
        return len(self._cards) == 0

    def contains(self, card):
        "Returns True if the specified card is in the deck, False otherwise."
        return card in self._cards

    def shuffle(self):
        """Shuffle the cards in the deck into a random order."""
        shuffle(self._cards)

    def deal(self):
        """If the deck is not empty, pop the card at the end of deck and return it."""
        if not self.is_empty():
            return self._cards.pop()

    def __str__(self):
        """Returs a printable string representation of cards in the deck."""
        return str(self._cards)

    def __repr__(self):
        """Returs a string representation of cards in the deck."""
        return self.__str__()

#Author: Aditya Dube (G02500368)