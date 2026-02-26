class Node:
    def __init__(self,info,next=None):
        self.info = info
        self.next = next

# creating singly linked list
class singlyLinkedlist:
    def __init__(self,head=None):
        self.head = head

    def insertATEnd(self,value):
        Node(value)
        if(self.head != None):
            t1 = self.head
        while(t1.next != None):
            t1 = t1.next
        else:
            self.head = temp

    def printLL(self):
        t1.head = self.head
        while(t1.nwxt!=None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)

obj =  singlyLinkedlist(10)
obj.insertATEnd(10)
obj.insertATEnd(20)
obj.insertATEnd(30)

obj.printLL()
