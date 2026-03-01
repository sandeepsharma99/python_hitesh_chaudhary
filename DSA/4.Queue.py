class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0 # check length of the array is  empty or not

    def insert(self,value):
        self.items.append(value) # insert at the end

    def delete(self):
        if(self.isEmpty()):
            print("Queue is empty")
        else:
           return self.items.pop(0) # deleteing from the beginning
        
q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)

print(q.delete())
print(q.delete())
print(q.delete())
q.delete()