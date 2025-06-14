size=int(input("Enter the Size of the List:"))
Num=[]
for i in range(size):
    Temp=int(input(f"Enter the element at {i} index:"))
    Num.append(Temp)
print(f"Given List:{Num}")
#max()--->prints the maximum number from the list
print("Maximum Element:",max(Num))
#min()-->prints the minimum number from the list
print("Minimum Element:",min(Num))

print("Summation:",sum(Num))
print("Sorted List:",sorted(Num))
 