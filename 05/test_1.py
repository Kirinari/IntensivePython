"""
test module for tictac game
"""

import unittest

from tictac import TicTacGame

class TestTicTac(unittest.TestCase):
    """
    unittest for tictac
    """
    def setUp(self) -> None:
        self.game = TicTacGame()

    def test_validate_input1(self):
        self.assertFalse(self.game.validate_input("hello"))

    def test_validate_input2(self):
        self.game.board[0][0] = 1
        self.assertFalse(self.game.validate_input("1 1"))

    def test_validate_input3(self):
        self.assertFalse(self.game.validate_input("4 4"))
    
    def test_validate_input5(self):
        self.game.board[0][0] = 1
        self.game.board[1][1] = 2
        self.game.board[2][2] = 1
        self.assertEqual(self.game.board, [[1, 0, 0], [0, 2, 0], [0, 0, 1]])

    def test_board(self):
        self.assertEqual(self.game.board, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_check_winner1(self):
        self.game.board[0][0] = 1
        self.game.board[1][1] = 1
        self.game.board[2][2] = 1
        self.game.check_winner()
        self.assertEqual(self.game.winner, 1)

    def test_check_winner2(self):
        self.game.board[0][0] = 1
        self.game.board[0][1] = 1
        self.game.board[0][2] = 1
        self.game.check_winner()
        self.assertEqual(self.game.winner, 1)

    def test_check_winner3(self):
        self.game.board[1][0] = 1
        self.game.board[1][1] = 1
        self.game.board[1][2] = 1
        self.game.check_winner()
        self.assertEqual(self.game.winner, 1)

    def test_check_winner4(self):
        self.game.board[2][0] = 1
        self.game.board[2][1] = 1
        self.game.board[2][2] = 1
        self.game.check_winner()
        self.assertEqual(self.game.winner, 1)

    def test_check_winner5(self):
        self.game.board[0][0] = 1
        self.game.board[1][0] = 1
        self.game.board[2][0] = 1
        self.game.check_winner()
        self.assertEqual(self.game.winner, 1)

    def test_check_winner6(self):
        self.game.board[0][1] = 1
        self.game.board[1][1] = 1
        self.game.board[2][1] = 1
        self.game.check_winner()
        self.assertEqual(self.game.winner, 1)

    def test_check_winner7(self):
        self.game.board[0][2] = 1
        self.game.board[1][2] = 1
        self.game.board[2][2] = 1
        self.game.check_winner()
        self.assertEqual(self.game.winner, 1)
    
    def test_check_winner8(self):
        self.game.board[0][2] = 1
        self.game.board[1][1] = 1
        self.game.board[2][0] = 1
        self.game.check_winner()
        self.assertEqual(self.game.winner, 1)

    def test_check_winner9(self):
        self.game.board[0][0] = 1
        self.game.board[1][0] = 1
        self.game.board[2][1] = 1
        self.game.board[0][2] = 1
        self.game.board[2][2] = 1
        self.game.board[0][1] = 2
        self.game.board[1][1] = 2
        self.game.board[1][2] = 2
        self.game.board[2][0] = 2
        self.game.check_winner()
        self.assertEqual(self.game.winner, 0)
        
    def test_check_winner10(self):
        self.game.board[0][0] = 2
        self.game.board[1][1] = 2
        self.game.board[2][2] = 2
        self.game.check_winner()
        self.assertEqual(self.game.winner, 2)

    def test_check_winner11(self):
        self.game.board[0][0] = 2
        self.game.board[0][1] = 2
        self.game.board[0][2] = 2
        self.game.check_winner()
        self.assertEqual(self.game.winner, 2)

    def test_check_winner12(self):
        self.game.board[1][0] = 2
        self.game.board[1][1] = 2
        self.game.board[1][2] = 2
        self.game.check_winner()
        self.assertEqual(self.game.winner, 2)

    def test_check_winner13(self):
        self.game.board[2][0] = 2
        self.game.board[2][1] = 2
        self.game.board[2][2] = 2
        self.game.check_winner()
        self.assertEqual(self.game.winner, 2)

    def test_check_winner14(self):
        self.game.board[0][0] = 2
        self.game.board[1][0] = 2
        self.game.board[2][0] = 2
        self.game.check_winner()
        self.assertEqual(self.game.winner, 2)

    def test_check_winner15(self):
        self.game.board[0][1] = 2
        self.game.board[1][1] = 2
        self.game.board[2][1] = 2
        self.game.check_winner()
        self.assertEqual(self.game.winner, 2)

    def test_check_winner16(self):
        self.game.board[0][2] = 2
        self.game.board[1][2] = 2
        self.game.board[2][2] = 2
        self.game.check_winner()
        self.assertEqual(self.game.winner, 2)
    
    def test_check_winner17(self):
        self.game.board[0][2] = 2
        self.game.board[1][1] = 2
        self.game.board[2][0] = 2
        self.game.check_winner()
        self.assertEqual(self.game.winner, 2)

if __name__ == '__main__':
    unittest.main()
