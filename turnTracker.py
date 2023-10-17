start = None
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = self
        self.prev = self


class TurnTracker:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0
        self._reversed = False
        self.L = []
        self._skipping = False

    def addPlayer(self, player):
        new_node = Node(player)
        current = self._head

        if self._length == 0 and not self._head and not self._tail:
            self._head = new_node
            self._tail = new_node

        else:
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node
        self._length += 1
        self.L.append(new_node.data)

    def insertStart(self, value):
        new_node = Node(value)
        current = self._head

        if self._length == 0 and not self._head and not self._tail:
            self._head = new_node
            self._tail = new_node

        else:
            self._head.prev = new_node
            new_node.next = self._head
            self._head = new_node
        self.L.insert(0, new_node.data)
        self._length += 1

    def removeEnd(self):
        self.L.pop()
        print(self.L)
        self._length -= 1

    def nextPlayer(self):  ##does not work yet
        self._skipping = False
        foward = []
        back = []

        if self._reversed is False:

            for i in self.L:
                foward.append(i)
            temp = foward[0]

            if temp:
                #print(temp)
                foward.pop(0)
                foward.append(temp)
                self.L = foward
                return temp

        elif self._reversed is True:

            for i in self.L:
                back.insert(0, i)
            temp = back[0]

            if temp:
                #print(temp)
                back.pop(0)
                back.append(temp)
                self.L = back
                return temp

    def skipNextPlayer(self):
        self._skipping = True
        return self.nextPlayer()

    def numberOfPlayers(self):
        return self._length

    def reverseTurnOrder(self):
        if self._reversed == False:
            self._reversed = True
        elif self._reversed == True:
            self._reversed = False


        '''if self._head != None:
            node_prev = self._head
            node_temp = self._head
            node_cur = self._head.next

            node_prev.next = node_prev
            node_prev.prev = node_prev

        while(node_cur != self._head):
            node_temp = node_cur.next
            node_cur.next = node_prev
            node_prev.prev = node_cur
            self._head.next = node_cur
            node_cur.prev = self._head

            node_prev = node_cur
            node_cur = node_temp

        self._head = node_prev
        for i in range(0, 5):
            self.reverseTurnOrder()'''


tt = TurnTracker()
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

