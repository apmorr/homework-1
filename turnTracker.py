class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None
      
class TurnTracker:
    def __init__(self):
      self.head = None
      self.tail = None
      self.size = 0
      
    def addPlayer(self, player):
        new_node = Node(player)
        current = self.Head
        if self.size == 0 and not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
        
        
        
        
        
    
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

