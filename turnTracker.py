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
        
        temp = self._head
        current = None
        
        if(temp):
            current = temp.data
            self.addPlayer(temp.data)
            self._count -= 1
            self._prev = temp
            self._head = temp.next
        return current

        '''temp =self._head
        current = None
        if (temp):
            current = temp.data
            self.addPlayer(current)
            temp = temp.next
        self.head = temp
        return temp.data'''
        
            
    def skipNextPlayer(self):
        #print(self.L)
        #temp = self.L[len(self.L)-1]
        #print(temp)
        temp = self.L[0]
        self.L.pop(0)
        self.L.append(temp)
        print(self.L)


    def numberOfPlayers(self):
        return self._count

        
    def reverseTurnOrder(self):
        temp = []
        for x in self.L:
            temp.insert(0, x)
        self.L = temp
        return self.L

    def reverseTurnOrder(self):
        self.printTT()
        elems = []
        temp = None
        cur = None
        first = self._head
        last = self._tail
        temp = self._head
        cur = self._tail
        self._tail = temp
        self._head = cur
        for x in range(self._count):
            
            temp = self._head.next
            cur = self._tail.prev
            
            self._tail.prev = temp
            self._head.next = cur
            
        
    def printTT(self):
        cur = self._head
        print('traverse foward')
        temp = cur
        while cur.next!=None:
            print(temp.data, end=" ")
            temp = temp.next
            

        '''current_node = self._head
        elem = []
        temp = current_node.next
        while current_node != None:
            current_node = current_node.next
            elem.append(current_node.data)'''

       


tt = TurnTracker()
tt.addPlayer(77)
tt.addPlayer(45)
tt.addPlayer(82)
tt.addPlayer(10)
tt.printTT()
'''print(tt.nextPlayer())
print(tt.nextPlayer())
print(tt.nextPlayer())
print(tt.nextPlayer())
print(tt.nextPlayer())
print(tt.numberOfPlayers())'''

