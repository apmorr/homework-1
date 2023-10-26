import unittest

class Chessboard:
    def __init__(self, size, k_idx, p_idxs):
        self.size = size
        self.k_idx = k_idx
        self.p_idxs = p_idxs
        self.visited = set()

    def valid_moves(self, k_idx):
        moves = []
        x, y = k_idx
        for dx, dy in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < self.size and 0 <= new_y < self.size:
                moves.append((new_x, new_y))
        return moves

    def solveable(self):
        if not self.p_idxs:
            return True  # No pawns left, the board is solvable

        if self.k_idx in self.visited:
            return False  # Knight visited this cell before

        self.visited.add(self.k_idx)

        for move in self.valid_moves(self.k_idx):
            if move in self.p_idxs:
                new_board = Chessboard(self.size, move, self.p_idxs - {move})
                if new_board.solveable():
                    return True

        return False

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
