import unittest
from hw5 import Chessboard

class TestChessboard(unittest.TestCase):
    def test_solvable_board(self):
        chessboard1 = Chessboard(8, (3, 3), {(1, 3), (2, 1), (2, 5), (4, 2), (5, 5), (6, 3)})
        self.assertTrue(chessboard1.solveable(), "Test Case 1: Solvable board is not marked as solvable")

    def test_unsolvable_board(self):
        chessboard2 = Chessboard(8, (3, 3), {(2, 1), (2, 5), (4, 2), (5, 5), (6, 3)})
        self.assertFalse(chessboard2.solveable(), "Test Case 2: Unsolvable board is marked as solvable")

    def test_no_pawns(self):
        chessboard3 = Chessboard(8, (3, 3), set())
        self.assertTrue(chessboard3.solveable(), "Test Case 3: No pawns on the board is marked as unsolvable")

if __name__ == '__main__':
    unittest.main()
