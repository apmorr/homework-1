class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      
class TurnTracker:
    def __init__(self):
      self.head = None
      self.prev = None
      self.L = list()
      
    def addPlayer(self, player):
        new_node = Node(player)
        self.L.append(player)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = new_node
        
        
        
    
    def nextPlayer(self):
        #tList = self.L
        temp = self.L[0]
        if temp:
            print(temp)
            self.L.pop(0)
            self.L.append(temp)
            
    def skipNextPlayer(self):
        #print(self.L)
        #temp = self.L[len(self.L)-1]
        #print(temp)
        temp = self.L[0]
        self.L.pop(0)
        self.L.append(temp)
        print(self.L)


    def numberOfPlayers(self):
        print(len(self.L))
        
        
    def reverseTurnOrder(self):
        temp = []
        for x in self.L:
            temp.insert(0, x)
        self.L = temp
        return self.L
        
    def printTT(self):
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next
       


tt = TurnTracker()
tt.addPlayer('james')
tt.addPlayer('mike')
tt.addPlayer('bella')

print('----')
tt.nextPlayer()
tt.nextPlayer()
tt.nextPlayer()
tt.nextPlayer()
print('---')
tt.skipNextPlayer()
print('----------')
tt.nextPlayer()
tt.nextPlayer()
tt.nextPlayer()
tt.nextPlayer()
print('---')
tt.numberOfPlayers()
print('---')
print(tt.reverseTurnOrder())


print('--')
tt.printTT()

