List=[12,24,67,98,98,76,45,3,25,16]
print("Original List:")
print(List)
New_List=[]
for i in List:
    if i not in New_List:
         New_List.append(i)
print(New_List)