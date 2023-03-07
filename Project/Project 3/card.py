class Card(object):
    """Card class models a card used in a deck of a playing cards."""

    def __init__(self, rank, suit):
        """
        Initializes a Card object with given rank and suit values.
        
        Parameters:
            rank (int): rank value for card
                        Valid values for rank are 1 to 13, both ends inclusive
                        1 (Ace), 2..10, 11 (Jack), 12 (Queen), 13 (King)

            suit (int): suit value for card
                        Valid values for suit are 1 to 4, both ends inclusive
                        1 (Clubs), 2 (Diamonds), 3 (Hearts), 4 (Spades)

        Instance variable:
            self._rank (int): initialized with value of parameter rank
            self._suit (int): initialized with value of parameter suit

        Validations and exceptions raised:
            Raise ValueError exception if parameter rank is not in the range 1 - 13
            Raise ValueError exception if parameter suit is not in the range 1 - 4
        """
        if not (1 <= rank <= 13):
            raise ValueError("Invalid rank value for card. Valid values are 1 to 13, both ends inclusive.")
        if not (1 <= suit <= 4):
            raise ValueError("Invalid suit value for card. Valid values are 1 to 4, both ends inclusive.")
        self._rank = rank
        self._suit = suit

    def get_rank(self):
        """Return the rank value of self Card object."""
        return self._rank

    def get_rank_as_string(self):
        """
        Returns the rank value as a string: "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"
        """
        rank_strings = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        return rank_strings.get(self._rank, str(self._rank))

    def get_suit(self):
        """Return the suit value of self Card object."""
        return self._suit
    
    def get_suit_as_string(self):
        """
        Returns the suit value as a string: "Clubs", "Diamonds", "Hearts", "Spades"
        """
        suit_strings = {1: "Clubs", 2: "Diamonds", 3: "Hearts", 4: "Spades"}
        return suit_strings.get(self._suit)

    def __str__(self):
        """Returns a printable string representation of Card object."""
        return self.get_rank_as_string() + " of " + self.get_suit_as_string()

    def __repr__(self):
        """Returns a string representation of Card object."""
        return self.__str__()

    def __eq__(self, other):
        """Returns True if self object is value equal to other object, False otherwise."""
        if isinstance(other, Card):
            return self._rank == other._rank and self._suit == other._suit
        return False


#Author: Aditya Dube (G02500368)