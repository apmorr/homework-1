class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.last = None

class TurnTracker:
    def __init__(self):
      self.head = None
      self.last = None
      self.prev = None
     
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
            
    def nextPlayer(self):
        temp = self.head
        current = None
        
        if(temp):
            current = temp.data
            self.addPlayer(temp.data)
            self.prev = temp
            self.head = temp.next
        return current

    def numberOfPlayers(self):
        current_node = self.head
        num = 0
        while(current_node):
            current_node = current_node.next
            num += 1
        print(num)
    
    def skipNextPlayer(self):
        temp = self.head
        self.addPlayer(temp.data)
        #print(temp.data, 'yo')
        self.prev = temp
        self.head = temp.next
        current = self.head
        
        #print(current.data, 'hey')
            
    def reverseTurnOrder(self):
        prev = None
        current = self.head
        temp = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev.next
        self.addPlayer(prev.data)
        
        
            

            
    
tt = TurnTracker()
tt.addPlayer('Jake')
tt.addPlayer('Lina')
tt.addPlayer('Tim')

tt.printTT()
print('---')
print(tt.nextPlayer())
print(tt.nextPlayer())
print(tt.nextPlayer())
tt.reverseTurnOrder()
print(tt.nextPlayer())
print('--')
tt.printTT()

#tt.numberOfPlayers()


