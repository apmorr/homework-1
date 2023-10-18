class Node:
    def __init__(self, player): #this creates a node
        self.player = player #this is the data stored in the node, NOT THE ADRESS
        self.next = None #this is the ADDRESS for the next node in the list
        self.prev = None #this isthe ADRESS for the previous node in the list

class TurnTracker:
    def __init__(self):
        self._head = None #represents the node at the front of the list
        self._tail = None #represents the node at the end of the list
        self._nextPlayer = None 
        self._length = 0
        self._reversed = False
        self._skipping = False

    def addPlayer(self, player):
        """adds a player to turn tracker"""
        new_node = Node(player) #when 'Node(player)' is called, it creates a entire new node
                                #'player' is the data assigned and the variable assigned 'new_node' is the adress
                                # The new node looks like (.prev=None[.player=data].next=None)
                                #the .next and .prev variables will be assigned to the adresses of differnt nodes
                                
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
        """returns next player"""
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
            current_player = self._nextPlayer.player

        return current_player

    def numberOfPlayers(self):
        """returns number of players"""
        return self._length

    def skipNextPlayer(self):
        """causes next player to be skipped"""
        if not self._reversed:
            if not self._skipping:
                # Skip one
                self._nextPlayer = self._nextPlayer.next

            else:
                # skip two
                for _ in range(2):
                    self._nextPlayer = self._nextPlayer.next

        else:
            if not self._skipping:
                # Skip one
                self._nextPlayer = self._nextPlayer.prev

            else:
                # Skip two
                for _ in range(2):
                    self._nextPlayer = self._nextPlayer.prev

        
        
    def reverseTurnOrder(self):
        """reverses direction"""
        
        if not self._reversed:
            self._nextPlayer = self._nextPlayer.prev
            self._reversed = True
              
        else: 
            self._nextPlayer = self._nextPlayer.next
            self._reversed = False
