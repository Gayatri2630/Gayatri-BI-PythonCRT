'''
Write a python program to create a customer service by adding the customer into the queue and once the customer is served 
he has to be removed from the queue

from collections import deque
queue=deque()
queue.append('Gayatri')
queue.append('Sahithi')
queue.append('Kavitha')
print(queue)
first=queue.popleft()
second=queue.popleft()
third=queue.popleft()
print(f"{first} customer is removed after service is done")
print(f"{second} customer is removed after service is done")
print(f"{third} customer is removed after service is done")
print("Queue after dequeuing:",queue)
'''
class Customer:
    def __init__(self):
        self.service=[]
    def enqueue(self,customer):
        self.service.append(customer)
        print("Customer is Added")
    def dequeue(self):
        if (len(self.service)>1):
            self.service.pop()
            print(f"{self.service.pop()} is removed")
        else:
            print("No customers left")
c1=Customer()
c1.enqueue('Gayatri')
c1.enqueue('Sahith')
c1.enqueue('Kavitha')
c1.dequeue()
c1.dequeue()
c1.dequeue()

