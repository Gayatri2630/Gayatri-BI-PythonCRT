from collections import deque
stack=deque()
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack after pushing:",stack)
top=stack.pop()
print("Popped Element:",top)
print("Stack after popping:",stack)
if not stack:
    print("Stack is Empty")
else:
    print("Stack is not Empty")
print("Top element:",stack[-1])