'''
Write python program to:
-->Take a list of toy names
-->Remove duplicates
-->Sort and display the list of toys
'''
size=int(input("Enter the Size of List:"))
Toy_List=[]
Newtoy_List=[]
for i in range(size):
    temp=input(f"Enter the element at {i} index:")
    Toy_List.append(temp)
print(Toy_List)
for i in Toy_List:
    if i not in Newtoy_List:
        Newtoy_List.append(i)
print("After removing Duplicates:",Newtoy_List)
Newtoy_List.sort()
print("Sorted List:",Newtoy_List)