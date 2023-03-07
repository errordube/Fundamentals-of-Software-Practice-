#
#  IMPORTANT: DO NOT MAKE ANY CHANGES TO THIS FILE
#

# import module that defines unit-testing framework
import unittest

# import classes from card and deck modules
from card import Card
from deck import Deck

class Project3Test(unittest.TestCase):

    def test_card_1(self):
        c = Card(5,1)
        self.assertEqual(c.get_rank(),5)
        self.assertEqual(c.get_suit(),1)

    def test_card_2(self):
        c = Card(5,2)
        self.assertEqual(c.get_rank(),5)
        self.assertEqual(c.get_suit(),2)

    def test_card_3(self):
        c = Card(5,3)
        self.assertEqual(c.get_rank(),5)
        self.assertEqual(c.get_suit(),3)

    def test_card_4(self):
        c = Card(5,4)
        self.assertEqual(c.get_rank(),5)
        self.assertEqual(c.get_suit(),4)

    def test_card_5(self):
        with self.assertRaises(ValueError):
            Card(0,1)
        
    def test_card_6(self):
        with self.assertRaises(ValueError):
            Card(14,1)

    def test_card_7(self):
        with self.assertRaises(ValueError):
            Card(1,0)

    def test_card_8(self):
        with self.assertRaises(ValueError):
            Card(1,5)

    def test_card_9(self):
        c = Card(1,1)
        self.assertEqual(c.get_rank_as_string(),"Ace")
        self.assertEqual(c.get_suit_as_string(),"Clubs")

    def test_card_10(self):
        c = Card(5,1)
        self.assertEqual(c.get_rank_as_string(),"5")
        self.assertEqual(c.get_suit_as_string(),"Clubs")

    def test_card_11(self):
        c = Card(11,2)
        self.assertEqual(c.get_rank_as_string(),"Jack")
        self.assertEqual(c.get_suit_as_string(),"Diamonds")

    def test_card_12(self):
        c = Card(12,3)
        self.assertEqual(c.get_rank_as_string(),"Queen")
        self.assertEqual(c.get_suit_as_string(),"Hearts")

    def test_card_13(self):
        c = Card(13,4)
        self.assertEqual(c.get_rank_as_string(),"King")
        self.assertEqual(c.get_suit_as_string(),"Spades")

    def test_card_14(self):
        c = Card(1,1)
        self.assertEqual(c.__repr__(),"Ace of Clubs")

    def test_card_15(self):
        c = Card(11,2)
        self.assertEqual(c.__repr__(),"Jack of Diamonds")

    def test_card_16(self):
        c = Card(12,3)
        self.assertEqual(c.__repr__(),"Queen of Hearts")

    def test_card_17(self):
        c = Card(13,4)
        self.assertEqual(c.__repr__(),"King of Spades")

    def test_card_18(self):
        c1 = Card(1,1)
        c2 = Card(1,1)
        self.assertTrue(c1 == c2)

    def test_card_19(self):
        c1 = Card(1,1)
        c2 = Card(4,3)
        self.assertTrue(c1 != c2)

    def test_card_20(self):
        c = Card(1,1)
        self.assertFalse(c == "Apple")

    def test_deck_1(self):
        deck = Deck()
        self.assertEqual(deck.size(),52)
        self.assertFalse(deck.is_empty())
        for rank in range(1,14):
            for suit in range(1,5):
                self.assertTrue(deck.contains(Card(rank,suit)))

    def test_deck_2(self):
        with self.assertRaises(ValueError):
            deck = Deck()
            deck.contains(Card(0,0))

    def test_deck_3(self):
        with self.assertRaises(ValueError):
            deck = Deck()
            deck.contains(Card(14,5))

    def test_deck_4(self):
        deck = Deck()
        cards_before_shuffle = []
        for i in range(52):
            cards_before_shuffle.append(deck.deal())
        deck = Deck()
        deck.shuffle()
        cards_after_shuffle = []
        for i in range(52):
            cards_after_shuffle.append(deck.deal())
        self.assertNotEqual(cards_before_shuffle,cards_after_shuffle)

    def test_deck_5(self):
        deck = Deck()
        card = deck.deal()
        self.assertFalse(deck.contains(card))
        self.assertEqual(deck.size(),51)

    def test_deck_6(self):
        deck = Deck()
        deck.deal()
        deck.deal()
        deck.deal()
        self.assertEqual(deck.size(),49)

    def test_deck_7(self):
        deck = Deck()
        card1 = deck.deal()
        card2 = deck.deal()
        self.assertTrue(card1 != card2)

    def test_deck_8(self):
        deck = Deck()
        for i in range(52):
            deck.deal()
        self.assertTrue(deck.is_empty())
        self.assertEqual(deck.size(),0)

    def test_deck_9(self):
        deck = Deck()
        for i in range(52):
            deck.deal()
        card = deck.deal()
        self.assertEqual(card,None)
        self.assertTrue(card is None)

    def test_deck_10(self):
        deck = Deck()
        expected = []
        for i in range(52):
            expected.append(deck.deal())
        expected.reverse()
        deck = Deck()
        self.assertEqual(deck.__repr__(),str(expected))

# run the unit tests in this script
if __name__ == '__main__':
    unittest.main(verbosity=2)
