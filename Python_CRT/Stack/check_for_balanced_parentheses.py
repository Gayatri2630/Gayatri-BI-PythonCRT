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
    def Check_balance(self):
        if '([{' in self.Stack:
            if self.Stack[3:]=='}])':
                print("Balanced Parentheses")
        elif '({[' in self.Stack:
            if self.Stack[3:]==']})':
                print("Balanced Parentheses")
        elif '{[(' in self.Stack:
            if self.Stack[3:]==')]}':
                print("Balanced Parentheses")    
        elif '[{(' in self.Stack:
            if self.Stack[3:]==')}]':
                print("Balanced Parentheses")  
        elif '[({' in self.Stack:
            if self.Stack[3:]=='})]':
                print("Balanced Parentheses")  
stack=Stack()
stack.push('([{}])')
stack.Check_balance()
