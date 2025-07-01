class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.append(item)
    def is_empty(self):
        return len(self.items)==0
    def dequeue(self,item):
        if self.is_empty():
            return None
        return self.items.pop(item)
    def peek_front(self):
        if self.is_empty():
            return None
        #return self.items[0]
        else:
            R=self.items[0]
            print(R)
    def peek_rear(self):
        if self.is_empty():
            return None
        #return self.items[-1]
        else:
            r=self.items[-1]
            print(r)
    def size(self):
        return len(self.items)
Q1=Queue()
Q1.enqueue(3)
Q1.enqueue(4)
Q1.enqueue(5)
Q1.enqueue(6)
Q1.peek_front()
Q1.peek_rear()
