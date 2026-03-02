
class circularQueue:
    def __init__(self,size):
        self.size = size
        self.item =[None]*size
        self.front = self.rear = -1


    def enqueue(self,value):
        if((self.rear+1)%self.size == self.front):
            print("Queue is Full")
        elif self.front == -1: 
            self.front = self.rear = 0
            self.item[self.rear] = value
        else:
            self.rear = (self.rear+1)%self.size
            self.item[self.rear] = value

    def dequeue(self):
        if(self.front==-1):
            print("Queue is Empty")
        elif self.front == self.rear:
            print(self.item[self.front])
            self.front = self.rear = -1
        else:
            print(self.item[self.front])
            self.front = (self.front+1)%self.size


cq = circularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)   # Queue is Full|
cq.dequeue()
cq.enqueue(60)
cq.enqueue(70)
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()