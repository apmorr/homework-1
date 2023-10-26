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
