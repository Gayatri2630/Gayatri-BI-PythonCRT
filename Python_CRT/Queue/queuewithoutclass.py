from collections import deque
queue=deque()
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue after enqueing:",queue)
first=queue.popleft()
print("Dequeued Element:",first)
print("Queue after dequeuing:",queue)
if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")
print("Front Element:",queue[0])