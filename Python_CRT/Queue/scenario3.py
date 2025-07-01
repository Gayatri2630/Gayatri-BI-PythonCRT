'''
write a python program the length of queue as input from the user and add the element by using enqueue method an dprint the elements present in the queue
and remove the elements one by one from the queue and check whether the queue is empty or not and print the front peekand rear peek
'''
from collections import deque
n=int(input("Enter the length of the Queue:"))
queue=deque()
for i in range(n):
    a=input("Enter the element:")
    queue.append(a)
print("Queue Elements:",queue)
print("Front Peek Element:",queue[0])
print("Rear Peek Element:",queue[-1])
if not queue:
    print("Queue is Empty")
else:
    print("Queue is not Empty")
for i in range(len(queue)):
    queue.popleft()
    print("Dequeued Element:",queue)

