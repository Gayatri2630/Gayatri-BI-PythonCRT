class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        new=Node(data)
        if not self.head:
            self.head=new
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
    def Display_List(self):
        current=self.head
        while current:
            print(current.data,end=" -> ")
            current=current.next
        print("None")
L1=LinkedList()
L1.insert_end(25.89)
L1.insert_end(99.56)
L1.insert_end(76.54)
L1.insert_end(100)
L1.Display_List()