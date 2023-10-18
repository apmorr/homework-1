import unittest
from turnTracker import TurnTracker

class TestTurnTracker(unittest.TestCase):
    def test_next_player_sequence(self):
        tt = TurnTracker()
        tt.addPlayer("Jake")
        tt.addPlayer("Lina")
        tt.addPlayer("Tim")

        self.assertEqual(tt.nextPlayer(), "Jake")
        self.assertEqual(tt.nextPlayer(), "Lina")
        self.assertEqual(tt.nextPlayer(), "Tim")
        self.assertEqual(tt.nextPlayer(), "Jake")
        self.assertEqual(tt.numberOfPlayers(), 3)

    def test_reverse_turn_order(self):
        tt = TurnTracker()
        tt.addPlayer("Jake")
        tt.addPlayer("Lina")
        tt.addPlayer("Tim")
        tt.reverseTurnOrder()

        self.assertEqual(tt.nextPlayer(), "Tim")
        self.assertEqual(tt.nextPlayer(), "Lina")
        self.assertEqual(tt.nextPlayer(), "Jake")

    def test_skip_next_player(self):
        tt = TurnTracker()
        tt.addPlayer("Jake")
        tt.addPlayer("Lina")
        tt.addPlayer("Tim")
        tt.skipNextPlayer()

        self.assertEqual(tt.nextPlayer(), "Lina")
        self.assertEqual(tt.nextPlayer(), "Tim")

if __name__ == "__main":
    unittest.main()
