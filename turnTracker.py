class Node:
    def __init__(self, data=None):
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
        # print(new_node.data)
        current = self._head
        if self._count == 0 and not self._head and not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node
        self._count += 1


    def nextPlayer(self):  ##does not work yet
        temp = self._head
        current = None
        if (temp):
            current = temp.data
            self.addPlayer(temp.data)
            self._count -= 1
            self._prev = temp
            self._head = temp.next
        return current


    def numberOfPlayers(self):
        return self._count


    def reverseTurnOrder(self):
        node1 = self._head
        node2 = self._tail
        temp = node1
        #print(node1.data)
        #print(node1.data, node2.data, temp.data)

        node1 = node2
        node2 = temp
        print(node1.data, node2.data) #node 1 is now node2

        node1 = node1.prev
        node2 = node2.next
        print(node1.data, node2.data)


        #print(node1.data)
        node1 = node1.prev
        node2 = node2.next
        print(node1.data, node2.data)
        node1 = node1.prev
        node2 = node2.next
        print(node1.data, node2.data)
        node1 = node1.prev
        node2 = node2.next
        print(node1.data, node2.data)
        node1 = node1.prev
        node2 = node2.next
        print(node1.data, node2.data)


    def printTT(self):
        cur = self._head
        for x in range(self._count):
            print(cur.data, end=' ')
            cur = cur.next


tt = TurnTracker()
tt.addPlayer(1)
tt.addPlayer(2)
tt.addPlayer(3)
tt.addPlayer(4)
tt.addPlayer(5)
tt.addPlayer(6)
tt.printTT()
print()
print('----------')
tt.reverseTurnOrder()
print('---------')
tt.printTT()

