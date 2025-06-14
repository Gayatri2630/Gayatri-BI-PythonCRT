size=int(input("Enter the Size of the List:"))
Num=[]
for i in range(size):
    Temp=int(input(f"Enter the element at {i} index:"))
    Num.append(Temp)
print(f"Given List:{Num}")
print(f"Reverse Elements of List:{Num[::-1]}")