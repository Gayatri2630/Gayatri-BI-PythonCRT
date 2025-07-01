'''
Problem:
Sort a list of names in a aplhabetical order using a sorting algorithm without built-in functions.

Input:
An integer n-number of names
A list of n names(strings of max length 100)

Output:
List of names sorted alphabetically 

Input:["Zara","John","Alex","Scott"]
Output:["Alex","John","Scott","Zara"]
'''
Arr=[]
n=int(input("Enter the number of  names:"))
for i in range(n):
    temp=input("Enter the name:")
    Arr.append(temp)
print(f"Names:{Arr}")
for i in range(len(Arr)):
    for j in range(len(Arr)-1):
        if (Arr[j]>Arr[j+1]):
            Arr[j],Arr[j+1]=Arr[j+1],Arr[j]
print(f"Sorted Names:{Arr}")