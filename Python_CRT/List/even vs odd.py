''' 
    write a python program to:
    --> input a list of elements
    --> create two new lists: one for odd numbers and one for even numbers 
    --> display both the lsits
''' 
size=int(input("Enter the size of List:"))
List=[]
for i in range(size):
    temp=int(input(f"Enter the value at {i} index:"))
    List.append(temp)
Even_List=[]
Odd_List=[]
for i in List:
    if i%2==0:
        Even_List.append(i)
    else:
        Odd_List.append(i)
print("Even List:",Even_List)
print("Odd List:",Odd_List)