class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None
        self.tail=self.head
        self.length=0
    def insertAtStart(head,data):
        newNode=Node(data)
        newNode.next=head
        head=newNode
        print("Element is Inserted")
    def print_list(self):
        if self.head!=None:
            current_node=self.head
            while current_node!=None:
                print(current_node.data,end=' ')
                current_node=current_node.next
        else:
            print("Empty")
LT=LinkedList()
LT.insertAtStart(25)
LT.print_list()