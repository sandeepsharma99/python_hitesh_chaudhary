# class Node:
#     def __init__(self,info,next=None):
#         self.info = info
#         self.next = next

# # creating singly linked list
# class singlyLinkedlist:
#     def __init__(self,head=None):
#         self.head = head

#     def insertATEnd(self,value):
#         Node(value)
#         if(self.head != None):
#             t1 = self.head
#         while(t1.next != None):
#             t1 = t1.temp
#         else:
#             self.head = temp

#     def printLL(self):
#         t1.head = self.head
#         while(t1.next !=None):
#             print(t1.data)
#             t1 = t1.next
#         print(t1.data)

# obj =  singlyLinkedlist()
# obj.insertATEnd(10)
# obj.insertATEnd(20)
# obj.insertATEnd(30)

# obj.printLL()


class Node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next


class singlyLinkedlist:
    def __init__(self):
        self.head = None

    def insertATEnd(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        t1 = self.head
        while t1.next is not None:
            t1 = t1.next

        t1.next = new_node

    def printLL(self):
        t1 = self.head
        while t1 is not None:
            print(t1.info)
            t1 = t1.next


obj = singlyLinkedlist()
obj.insertATEnd(10)
obj.insertATEnd(20)
obj.insertATEnd(30)

obj.printLL()

class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next

class SinglyLinkedList:
    def __int__(self, head=None):
        self.head = head

    def insertAtEnd(self,value):
        Node(value)
        if(self.head != None):
            t1 = self.head
        while(t1.next !=None):
            t1 = t1.temp
        else:
            self.head = temp

    
