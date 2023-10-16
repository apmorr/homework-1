class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

class TurnTracker:
    def __init__(self):
      self.head = None
     
    def addPlayer(self, player):
        new_node = Node(player)
        if self.head is None:
            self.head = new_node
            return
            
        temp = self.head
        while(temp.next):
            temp = temp.next
            
        temp.next = new_node

    def printTT(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next
            
    #def nextPlayer(self):


    def numberOfPlayers(self):
        current_node = self.head
        num = 0
        while(current_node):
            current_node = current_node.next
            num += 1
        print(num)
    
    def skipNextPlayer(self):
        temp = self.head
        temp = temp.next.next

        print(temp.data)
    
    
    
tt = TurnTracker()
tt.addPlayer('james')
tt.addPlayer('mike')
tt.addPlayer('sam')
