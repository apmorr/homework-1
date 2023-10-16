class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.last = None

class TurnTracker:
    def __init__(self):
      self.head = None
      self.last = None
     
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
        
        if(temp):
            print(temp.data)
            self.addPlayer(temp.data)
            self.prev = temp
            self.head = temp.next
            
            
                


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
        
    
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
    
tt = TurnTracker()
tt.addPlayer('Jake')
tt.addPlayer('Lina')
tt.addPlayer('Tim')
tt.printLL()
tt.printTT()
print('------------')

tt.nextPlayer() #jake 1
tt.nextPlayer() #lina 2
tt.nextPlayer() #tim 3
tt.skipNextPlayer() #tim -> jake -> lina 
tt.nextPlayer() #lina 2
tt.skipNextPlayer() #lina -> tim -> jake
tt.nextPlayer() #jake 1
tt.nextPlayer() #lina 2





tt.numberOfPlayers()


