class Stack:
    def __init__(self):
        self.Stack=[]
    def push(self,data):
        self.Stack.append(data)
        print(f"{data} Element is Appended")
    def isempty(self):
        if len(self.Stack)==0:
            return True
    def pop(self,data):
        if self.isempty():
            print("Stack is empty")
        else:
            self.Stack.pop()
            print(f"{data} Element is removed")
    def peek(self):
        Len=len(self.Stack)
        print(f"Peek element is {self.Stack[Len-1]}")
    def size(self):
        Len=len(self.Stack)
        print(Len)
    def Display(self):
        for i in self.Stack:
            print(i)
stack=Stack()
stack.push(100)
stack.push(105)
stack.push(150)
stack.push(98)
stack.Display()
stack.size()