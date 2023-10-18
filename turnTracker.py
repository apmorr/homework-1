class Node:
    def __init__(self, player):
        self.player = player
        self.next = None
        self.prev = None

class TurnTracker:
    def __init__(self):
        self._head = None
        self._tail = None
        self._nextPlayer = None
        self._length = 0
        self._reversed = False
        self._skipping = False

    def addPlayer(self, player):
        """Adds a player to the turn tracker."""
        new_node = Node(player)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.prev = self._tail
            new_node.next = self._head
            self._tail.next = new_node
            self._head.prev = new_node
            self._tail = new_node

        if self._nextPlayer is None:
            self._nextPlayer = new_node

        self._length += 1
        
    def nextPlayer(self):
        """Returns the next player in the turn order based on the current game state."""
        if self._length == 0:
            raise RuntimeError("No players in the turn tracker.")

        if self._skipping:
            if not self._reversed:
                self._nextPlayer = self._nextPlayer.next
            else:
                self._nextPlayer = self._nextPlayer.prev

            self._skipping = False

        current_player = self._nextPlayer.player

        if not self._reversed:
            self._nextPlayer = self._nextPlayer.next
        else:
            self._nextPlayer = self._nextPlayer.prev

        return current_player

    def numberOfPlayers(self):
        """Returns the number of players in the turn tracker."""
        return self._length

    def skipNextPlayer(self):
        """Causes the next player in the turn order to be skipped."""
        if not self._reversed:
            if not self._skipping:
                # Skip one more player.
                self._nextPlayer = self._nextPlayer.next

            else:
                # Skip two more players.
                for _ in range(2):
                    self._nextPlayer = self._nextPlayer.next

        else:
            if not self._skipping:
                # Skip one more player.
                self._nextPlayer = self._nextPlayer.prev

            else:
                # Skip two more players.
                for _ in range(2):
                    self._nextPlayer = self._nextPlayer.prev

        # Set skipping to True.
        # If skipNextPlayer() is called again before nextPlayer(), it will skip two more players.
        # If nextPlayer() is called after skipNextPlayer(), it will skip one more player.
        # Either way, at least one player will be skipped.
        # This behavior is consistent with how the Skip card works in Uno.
        # If a player plays a Skip card, the next player in turn order is skipped.
        # If two players in a row play Skip cards, the next two players in turn order are skipped.
        # And so on...
        # This behavior can be changed by modifying this method.
        # For example, you could reset skipping to False at the end of this method to only skip one player per call to skipNextPlayer().
        # Or you could add a parameter to this method to specify how many players to skip.
        
    def reverseTurnOrder(self):
        """Reverses the current direction of the turn order."""
        self._nextPlayer = self._head


        if not self._reversed:
              self._reversed = True
        else: 
            self._reversed = False
# Example 1 usage 


tt = TurnTracker()
tt.addPlayer("Jake")
tt.addPlayer("Lina")
tt.addPlayer("Tim")
print(tt.nextPlayer())
print(tt.nextPlayer())
print(tt.nextPlayer())
print(tt.nextPlayer())
print(tt.numberOfPlayers())

 # Example 2
print ("Example 2")
tt= TurnTracker()
tt.addPlayer("Jake")
tt.addPlayer("Lina")
tt.addPlayer("Tim")
print(tt.nextPlayer())
print(tt.nextPlayer())
tt.reverseTurnOrder() # Lina plays reverse card
print(tt.nextPlayer())
print(tt.nextPlayer())
print(tt.nextPlayer())



#Example 3
print ("Example 3")

tt= TurnTracker()
tt.addPlayer("Jake")
tt.addPlayer("Lina")
tt.addPlayer("Tim")
print(tt.nextPlayer())
print(tt.nextPlayer()) 
print(tt.nextPlayer())
tt.skipNextPlayer() # Tim plays Skip card
print(tt.nextPlayer())
tt.skipNextPlayer() # Lina plays Skip card
print(tt.nextPlayer())
print(tt.nextPlayer())



#Example 4
print ("Example 4")

tt =TurnTracker()
tt.addPlayer("Jake")
tt.addPlayer("Lina")
tt.addPlayer("Tim")
print(tt.nextPlayer())
print(tt.nextPlayer())
print(tt.nextPlayer())
tt.skipNextPlayer()# Tim plays Skip card
print(tt.nextPlayer())
tt.reverseTurnOrder # Lina plays Reverse card
print(tt.nextPlayer())
tt.skipNextPlayer() # Jake plays Skip card
print(tt.nextPlayer())
print(tt.nextPlayer())


