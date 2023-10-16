class Node:
   def __init__(self, data = None):
      self.data = data
      self.next = self
      self.prev = self
      
class TurnTracker:
    def __init__(self):
      self._head = None
      self._tail = None
      self._count = 0
      
    def addPlayer(self, player):
        new_node = Node(player)
        #print(new_node.data)
        current = self._head
        if self._count == 0 and not self._head and not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node
        self._count += 1
        
    def remove(self, data): ##this works as intended
        cur = Node(data)
        temp = self._head
        #print(cur.data, temp.data, 'hey')
        if cur == temp:
            self.head = None
        temp = self.head
        #print(cur.data, temp.data, 'hi')
        
        
        
    def nextPlayer(self): ##does not work yet
        #tList = self.L
        temp = self._head
        if temp.next != None:
            self.head = temp.next
            self.remove(temp.data)
            self.addPlayer(temp.data)
            return temp.data
        else:
            return temp.prev
            
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
tt.addPlayer(77)
tt.addPlayer(45)
tt.addPlayer(82)
tt.addPlayer(10)
print(tt.nextPlayer())
print(tt.nextPlayer())
print(tt.nextPlayer())
