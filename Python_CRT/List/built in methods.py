cartoons=['Tom &Jerry','Doremon','Shinchan','Oggy &Cockroaches']
print(cartoons)
print("After Appending:")
cartoons.append('Heidi')
print(cartoons)
#Add another element
# append()---> add the element at the end of the list
cartoons.append('Smurfs')
print(cartoons)
# insert() ----> add the element at the specific position
print("After Inserting:")
cartoons.insert(0,'Chhota Bheem')
print(cartoons)
#pop()---> remove the element from the list
print("After pop:")
cartoons.pop() #remove the first elemnet from the list(using index)
print(cartoons)
cartoons.pop(0) # pop(n)---> remove the element from the given position
print(cartoons)
#remove()---> remove the element without using index
print("After removing:")
cartoons.remove('Oggy &Cockroaches')
print(cartoons)
#index()---> prints the position of the element in the list
print("Index of the Element:")
#x=cartoons.index('Tom &Jerry')
#print(x)
print(cartoons.index('Doremon'))
#reverse()--->inverts the list
print("After Reversing:")
cartoons.reverse()
print(cartoons)

