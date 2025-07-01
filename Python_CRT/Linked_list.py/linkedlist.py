class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_front(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
    def show(self):
        temp=self.head
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print("None")
#Example Usage
ll=LinkedList()
ll.insert_front(5)
ll.insert_front(15)
ll.insert_front(20)
ll.show()