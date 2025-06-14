size=int(input("Enter the Size of the List:"))
Num=[]
for i in range(size):
    Temp=int(input(f"Enter the element at {i} index:"))
    Num.append(Temp)
print(f"Given List:{Num}")
# sorting list using nested loops
for i in range(0, len(Num)):
    for j in range(i+1, len(Num)):
        if Num[i] >= Num[j]:
            Num[i], Num[j] = Num[j],Num[i]
# sorted list
print("Sorted List:",Num)