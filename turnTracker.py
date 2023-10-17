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
        self._rev = False

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

        current = self._tail
        temp = None
        last = self._head
        cur = None
        elem = []

        #print(self._tail.data, 'last')
        #print(current.data)
        #print(self._head.data, 'first')
        #print(self._head.data, self._head.next.data, self._tail.prev.data, self._tail.data)




        if self._head == self._tail:
            print('ok')
            for i in elem:
                print(i.data)


            #print(current.data, last.data, 'yo2')
            #print(self._head.data, self._head.next.data, self._head.next.next.data, self._tail.prev.data, self._tail.data, 'hey2')

            #temp = current
            #current = current.prev
            #print(temp.data, 'end')
            #current = last
            #self._tail = last
            #print(current.data)
        if current != None:
            #print(self._head.data, self._head.next.data, self._tail.prev.data, self._tail.data)

            #print(current.data, self._head.data, self._head.next.data, self._head.next.next.data, self._tail.prev.data, self._tail.data)

            #temp = self._head
            #print(current.data, self._head.data, self._head.next.data, self._head.next.next.data, self._tail.prev.data, self._tail.data)

            #print(current.data, self._head.data, self._head.next.data, self._head.next.next.data, self._tail.prev.data, self._tail.data)
            temp = current
            current = current.prev
            cur = last
            #last = last.next


            #print(self._head.data, self._head.next.data, self._head.next.next.data, self._tail.prev.data, self._tail.data, 'hey1')
            #print(temp.data, current.data, last.data, cur.data, 'yo1')
            if self._head == self._tail:
                print('cool', temp.data, current.data, last.data)


            self._tail = current
            self._head = temp
            self._head.next = last

            #temp = temp.next

            print(temp.data, current.data, last.data, cur.data, 'yo2')
            print(self._head.data, self._head.next.data, self._head.next.next.data, self._head.next.next.next.data, self._tail.data, 'hey2')


            print(self._head.data, elem, 'FINAL')
            if elem[len(elem) - 1] != self._head:
                elem.append(self._head)







            #current = current.prev
            #print(current.data, self._head.data, self._head.next.data, self._head.next.next.data, self._tail.prev.data, self._tail.data)

            #current = current.prev
            #self._head = current
            #print(temp.data, 'going')



        return self._head.next.data



        current = self._head
        temp = None

        if current.next != None:
            temp = current
            current = current.next
            self._head = current
            return(temp.data)




    def numberOfPlayers(self):
        return self._count


    def reverseTurnOrder(self):
        if self._rev == False:
            self._rev = True
        elif self._rev == True:
            self._rev = False


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



    def printTT(self):

        cur = self._head

        for x in range(self._count):
            print(cur.data, end=' ')
            cur = cur.next


tt = TurnTracker()
tt.addPlayer(10)
tt.addPlayer(20)
tt.addPlayer(30)
tt.addPlayer(40)
tt.addPlayer(50)
tt.nextPlayer()
tt.nextPlayer()
tt.nextPlayer()
tt.nextPlayer()
tt.nextPlayer()
tt.nextPlayer()
tt.nextPlayer()
tt.nextPlayer()
tt.nextPlayer()
tt.nextPlayer()




tt.printTT()


