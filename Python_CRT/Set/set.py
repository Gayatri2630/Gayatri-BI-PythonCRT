Set={10,20,30,40,50,60,70,80,90,100}
print(Set)
print(type(Set))
#accessing the element from the set
print(20 in Set)
#add()-adds the  single element to set
Set.add(110)
Set.add(120)
Set.add(130)
print(Set)
#update()-adds the multiple elements to set
Set2={140,150,160,170,180}
Set.update(Set2)
print(Set)
#remove()-to remove specific item from the set and raises an error if element is not present
Set.remove(10)
print(Set)
#pop()-removes element at begining of the set
Set.pop()
print(Set)
#discard()-removes specific element and does not raise an error if element is not present
Set.discard(100)
print(Set)
#clear()-remove all the elements from the set
Set.clear()
print(Set2)
#union(|)-returns all uniques items from both sets
Set1={1,2,3}
Set3={3,4,5}
print(Set1|Set3)
#intersection(&)-returns a common items from both the sets
print(Set1&Set3)
#difference(-)- return a set containing that are only in the first set and not in the second set
#symmetric difference(^)-returns a set containing items that are in either set,but not both
print(Set1-Set3)
print(Set1^Set3)
