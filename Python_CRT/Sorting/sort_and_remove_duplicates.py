'''
Problem:
Given a list of integers that amy contain duplicates,
sort the list in ascending order and remove all duplicates

Input:
A list of Interger arr with length n

Output:
Sorted list with unique elements only

Input:[4,2,2,8,4,6]
Output:[2,4,6,8]
'''
Arr=[4,2,2,8,4,6]
new_Arr=[]
print(f"Orginal List:{Arr} ")
for i in range(len(Arr)):
    for j in range(len(Arr)-1):
        if Arr[j]>Arr[j+1]:
            Arr[j],Arr[j+1]=Arr[j+1],Arr[j]
for i in Arr:
    if i not in new_Arr:
        new_Arr.append(i)
print(f"Sorted List:{new_Arr}")

