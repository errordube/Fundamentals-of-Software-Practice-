#
#  IMPORTANT: DO NOT MAKE ANY CHANGES TO THIS FILE
#

# import module that defines unit-testing framework
import unittest

from othello import Othello

class Project4Test(unittest.TestCase):

    def test_constructor_1(self):
        game = Othello(4,Othello.PLAYER1,Othello.BLACK)
        self.assertEqual(game.get_board_size(),4)
        self.assertEqual(game.get_turn(),Othello.PLAYER1)
        self.assertEqual(game.get_player_disc(Othello.PLAYER1),Othello.BLACK)
        self.assertEqual(game.get_player_disc(Othello.PLAYER2),Othello.WHITE)
        expected = "0 1 2 3\n0 - - - -\n1 - B W -\n2 - W B -\n3 - - - -"
        self.assertEqual(str(game).strip(),expected)

    def test_constructor_2(self):
        game = Othello(6,Othello.PLAYER2,Othello.WHITE)
        self.assertEqual(game.get_board_size(),6)
        self.assertEqual(game.get_turn(),Othello.PLAYER2)
        self.assertEqual(game.get_player_disc(Othello.PLAYER1),Othello.BLACK)
        self.assertEqual(game.get_player_disc(Othello.PLAYER2),Othello.WHITE)
        expected = "0 1 2 3 4 5\n0 - - - - - -\n1 - - - - - -\n2 - - B W - -\n3 - - W B - -\n4 - - - - - -\n5 - - - - - -"
        self.assertEqual(str(game).strip(),expected)

    def test_constructor_3(self):
        game = Othello(8,Othello.PLAYER1,Othello.BLACK)
        self.assertEqual(game.get_board_size(),8)
        self.assertEqual(game.get_turn(),Othello.PLAYER1)
        self.assertEqual(game.get_player_disc(Othello.PLAYER1),Othello.BLACK)
        self.assertEqual(game.get_player_disc(Othello.PLAYER2),Othello.WHITE)
        expected = "0 1 2 3 4 5 6 7\n0 - - - - - - - -\n1 - - - - - - - -\n2 - - - - - - - -\n3 - - - B W - - -\n4 - - - W B - - -\n5 - - - - - - - -\n6 - - - - - - - -\n7 - - - - - - - -"
        self.assertEqual(str(game).strip(),expected)

    def test_is_board_full_1(self):
        game = Othello(8,Othello.PLAYER1,Othello.BLACK)
        self.assertFalse(game.is_board_full())

    def test_is_board_full_2(self):
        game = Othello(4,Othello.PLAYER1,Othello.BLACK)
        game.place_disc_at_pos(1,3,Othello.BLACK)
        game.place_disc_at_pos(0,3,Othello.WHITE)
        self.assertFalse(game.is_board_full())

    def test_is_board_full_3(self):
        game = Othello(4,Othello.PLAYER1,Othello.BLACK)
        game.place_disc_at_pos(1,3,Othello.BLACK)
        game.place_disc_at_pos(0,3,Othello.WHITE)
        game.place_disc_at_pos(0,2,Othello.BLACK)
        game.place_disc_at_pos(0,1,Othello.WHITE)
        game.place_disc_at_pos(3,0,Othello.BLACK)
        game.place_disc_at_pos(3,2,Othello.WHITE)
        game.place_disc_at_pos(1,0,Othello.BLACK)
        game.place_disc_at_pos(2,0,Othello.WHITE)
        game.place_disc_at_pos(3,1,Othello.BLACK)
        game.place_disc_at_pos(3,3,Othello.WHITE)
        game.set_next_turn()
        game.place_disc_at_pos(0,0,Othello.WHITE)
        game.set_next_turn()
        game.place_disc_at_pos(2,3,Othello.WHITE)
        self.assertTrue(game.is_board_full())

    def test_is_a_valid_move_available_1(self):
        game = Othello(4,Othello.PLAYER1,Othello.BLACK)
        self.assertTrue(game.is_a_valid_move_available(Othello.WHITE))
        self.assertTrue(game.is_a_valid_move_available(Othello.BLACK))

    def test_is_a_valid_move_available_2(self):
        game = Othello(4,Othello.PLAYER1,Othello.BLACK)
        game.place_disc_at_pos(1,3,Othello.BLACK)
        game.place_disc_at_pos(0,3,Othello.WHITE)
        game.place_disc_at_pos(0,2,Othello.BLACK)
        game.place_disc_at_pos(0,1,Othello.WHITE)
        game.place_disc_at_pos(3,0,Othello.BLACK)
        game.place_disc_at_pos(3,2,Othello.WHITE)
        game.place_disc_at_pos(1,0,Othello.BLACK)
        game.place_disc_at_pos(2,0,Othello.WHITE)
        game.place_disc_at_pos(3,1,Othello.BLACK)
        game.place_disc_at_pos(3,3,Othello.WHITE)
        self.assertFalse(game.is_a_valid_move_available(Othello.BLACK))
        game.set_next_turn()
        game.place_disc_at_pos(0,0,Othello.WHITE)
        self.assertFalse(game.is_a_valid_move_available(Othello.BLACK))

    def test_valid_move_1(self):
        game = Othello(4,Othello.PLAYER1,Othello.BLACK)
        self.assertFalse(game.is_valid_move(0,0,Othello.BLACK))
        self.assertFalse(game.is_valid_move(0,1,Othello.BLACK))
        self.assertFalse(game.is_valid_move(0,3,Othello.BLACK))
        self.assertFalse(game.is_valid_move(1,0,Othello.BLACK))
        self.assertFalse(game.is_valid_move(2,3,Othello.BLACK))
        self.assertFalse(game.is_valid_move(3,0,Othello.BLACK))
        self.assertFalse(game.is_valid_move(3,2,Othello.BLACK))
        self.assertFalse(game.is_valid_move(3,3,Othello.BLACK))
        self.assertFalse(game.is_valid_move(0,0,Othello.WHITE))
        self.assertFalse(game.is_valid_move(0,2,Othello.WHITE))
        self.assertFalse(game.is_valid_move(0,3,Othello.WHITE))
        self.assertFalse(game.is_valid_move(1,3,Othello.WHITE))
        self.assertFalse(game.is_valid_move(2,0,Othello.WHITE))
        self.assertFalse(game.is_valid_move(3,0,Othello.WHITE))
        self.assertFalse(game.is_valid_move(3,1,Othello.WHITE))
        self.assertFalse(game.is_valid_move(3,3,Othello.WHITE))

    def test_valid_move_2(self):
        game = Othello(4,Othello.PLAYER1,Othello.BLACK)
        self.assertTrue(game.is_valid_move(0,2,Othello.BLACK))
        self.assertTrue(game.is_valid_move(1,3,Othello.BLACK))
        self.assertTrue(game.is_valid_move(2,0,Othello.BLACK))
        self.assertTrue(game.is_valid_move(3,1,Othello.BLACK))
        self.assertTrue(game.is_valid_move(0,1,Othello.WHITE))
        self.assertTrue(game.is_valid_move(1,0,Othello.WHITE))
        self.assertTrue(game.is_valid_move(2,3,Othello.WHITE))
        self.assertTrue(game.is_valid_move(3,2,Othello.WHITE))

    def test_4x4_board_play(self):
        game = Othello(4,Othello.PLAYER1,Othello.BLACK)
        game.place_disc_at_pos(1,3,Othello.BLACK)
        game.place_disc_at_pos(0,3,Othello.WHITE)
        game.place_disc_at_pos(0,2,Othello.BLACK)
        game.place_disc_at_pos(0,1,Othello.WHITE)
        game.place_disc_at_pos(3,0,Othello.BLACK)
        game.place_disc_at_pos(3,2,Othello.WHITE)
        game.place_disc_at_pos(1,0,Othello.BLACK)
        game.place_disc_at_pos(2,0,Othello.WHITE)
        game.place_disc_at_pos(3,1,Othello.BLACK)
        game.place_disc_at_pos(3,3,Othello.WHITE)
        game.set_next_turn()
        game.place_disc_at_pos(0,0,Othello.WHITE)
        game.set_next_turn()
        game.place_disc_at_pos(2,3,Othello.WHITE)
        self.assertTrue(game.is_board_full())
        self.assertFalse(game.is_a_valid_move_available(Othello.WHITE))
        self.assertFalse(game.is_a_valid_move_available(Othello.BLACK))
        self.assertTrue(game.is_game_over())
        self.assertEqual(game.who_won(),Othello.PLAYER2)

    def test_6x6_board_play(self):
        game = Othello(6,Othello.PLAYER2,Othello.WHITE)
        game.place_disc_at_pos(2,1,Othello.WHITE)
        game.place_disc_at_pos(1,3,Othello.BLACK)
        game.place_disc_at_pos(2,4,Othello.WHITE)
        game.place_disc_at_pos(3,5,Othello.BLACK)
        game.place_disc_at_pos(4,4,Othello.WHITE)
        game.place_disc_at_pos(2,0,Othello.BLACK)
        game.place_disc_at_pos(1,1,Othello.WHITE)
        game.place_disc_at_pos(0,1,Othello.BLACK)
        game.place_disc_at_pos(0,0,Othello.WHITE)
        game.place_disc_at_pos(4,1,Othello.BLACK)
        game.place_disc_at_pos(2,5,Othello.WHITE)
        game.place_disc_at_pos(4,3,Othello.BLACK)
        game.place_disc_at_pos(4,2,Othello.WHITE)
        game.place_disc_at_pos(4,5,Othello.BLACK)
        game.place_disc_at_pos(5,5,Othello.WHITE)
        game.place_disc_at_pos(1,2,Othello.BLACK)
        game.place_disc_at_pos(4,0,Othello.WHITE)
        game.place_disc_at_pos(5,3,Othello.BLACK)
        game.place_disc_at_pos(1,4,Othello.WHITE)
        game.place_disc_at_pos(0,3,Othello.BLACK)
        game.place_disc_at_pos(0,2,Othello.WHITE)
        game.place_disc_at_pos(5,0,Othello.BLACK)
        game.place_disc_at_pos(3,1,Othello.WHITE)
        game.place_disc_at_pos(0,5,Othello.BLACK)
        game.place_disc_at_pos(3,4,Othello.WHITE)
        game.place_disc_at_pos(5,4,Othello.BLACK)
        game.place_disc_at_pos(5,1,Othello.WHITE)
        game.place_disc_at_pos(1,0,Othello.BLACK)
        game.place_disc_at_pos(0,4,Othello.WHITE)
        game.place_disc_at_pos(5,2,Othello.BLACK)
        game.place_disc_at_pos(3,0,Othello.WHITE)
        game.set_next_turn()
        game.place_disc_at_pos(1,5,Othello.WHITE)
        self.assertTrue(game.is_game_over())
        self.assertEqual(game.who_won(),Othello.PLAYER2)

    def test_8x8_board_play(self):
        game = Othello(8,Othello.PLAYER1,Othello.BLACK)
        game.place_disc_at_pos(5,3,Othello.BLACK)
        game.place_disc_at_pos(5,2,Othello.WHITE)
        game.place_disc_at_pos(3,5,Othello.BLACK)
        game.place_disc_at_pos(2,5,Othello.WHITE)
        game.place_disc_at_pos(4,2,Othello.BLACK)
        game.place_disc_at_pos(3,6,Othello.WHITE)
        game.place_disc_at_pos(3,7,Othello.BLACK)
        game.place_disc_at_pos(3,2,Othello.WHITE)
        game.place_disc_at_pos(1,6,Othello.BLACK)
        game.place_disc_at_pos(0,7,Othello.WHITE)
        game.place_disc_at_pos(4,1,Othello.BLACK)
        game.place_disc_at_pos(5,4,Othello.WHITE)
        game.place_disc_at_pos(6,3,Othello.BLACK)
        game.place_disc_at_pos(6,2,Othello.WHITE)
        game.place_disc_at_pos(6,1,Othello.BLACK)
        game.place_disc_at_pos(7,2,Othello.WHITE)
        game.place_disc_at_pos(7,1,Othello.BLACK)
        game.place_disc_at_pos(2,3,Othello.WHITE)
        game.place_disc_at_pos(3,1,Othello.BLACK)
        game.place_disc_at_pos(2,4,Othello.WHITE)
        game.place_disc_at_pos(6,5,Othello.BLACK)
        game.place_disc_at_pos(6,0,Othello.WHITE)
        game.place_disc_at_pos(1,4,Othello.BLACK)
        game.place_disc_at_pos(2,6,Othello.WHITE)
        game.place_disc_at_pos(7,3,Othello.BLACK)
        game.place_disc_at_pos(5,5,Othello.WHITE)
        game.place_disc_at_pos(4,5,Othello.BLACK)
        game.place_disc_at_pos(4,6,Othello.WHITE)
        game.place_disc_at_pos(4,7,Othello.BLACK)
        game.place_disc_at_pos(2,0,Othello.WHITE)
        game.place_disc_at_pos(5,1,Othello.BLACK)
        game.place_disc_at_pos(6,4,Othello.WHITE)
        game.place_disc_at_pos(3,0,Othello.BLACK)
        game.place_disc_at_pos(2,2,Othello.WHITE)
        game.place_disc_at_pos(1,2,Othello.BLACK)
        game.place_disc_at_pos(5,6,Othello.WHITE)
        game.place_disc_at_pos(5,7,Othello.BLACK)
        game.place_disc_at_pos(0,2,Othello.WHITE)
        game.place_disc_at_pos(2,7,Othello.BLACK)
        game.place_disc_at_pos(6,6,Othello.WHITE)
        game.place_disc_at_pos(7,4,Othello.BLACK)
        game.place_disc_at_pos(7,5,Othello.WHITE)
        game.place_disc_at_pos(6,7,Othello.BLACK)
        game.place_disc_at_pos(7,0,Othello.WHITE)
        game.place_disc_at_pos(0,6,Othello.BLACK)
        game.place_disc_at_pos(5,0,Othello.WHITE)
        game.place_disc_at_pos(4,0,Othello.BLACK)
        game.place_disc_at_pos(7,6,Othello.WHITE)
        game.place_disc_at_pos(2,1,Othello.BLACK)
        game.place_disc_at_pos(1,5,Othello.WHITE)
        game.place_disc_at_pos(1,3,Othello.BLACK)
        game.place_disc_at_pos(7,7,Othello.WHITE)
        game.place_disc_at_pos(0,5,Othello.BLACK)
        game.place_disc_at_pos(1,7,Othello.WHITE)
        game.place_disc_at_pos(0,3,Othello.BLACK)
        game.place_disc_at_pos(0,4,Othello.WHITE)
        game.place_disc_at_pos(1,0,Othello.BLACK)
        game.place_disc_at_pos(0,1,Othello.WHITE)
        game.place_disc_at_pos(1,1,Othello.BLACK)
        game.place_disc_at_pos(0,0,Othello.WHITE)
        self.assertTrue(game.is_game_over())
        self.assertEqual(game.who_won(),Othello.PLAYER2)               


# run the unit tests if the script is run as a top-level program
if __name__ == '__main__':
    unittest.main(verbosity=2)