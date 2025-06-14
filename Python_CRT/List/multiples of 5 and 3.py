size=int(input("Enter the Size of List:"))
Num=[]
New_Num=[]
for i in range(size):
    Temp=int(input(f"Enter the element at {i} index:"))
    Num.append(Temp)
print("Original List:")
print(Num)
for i in Num:
    if(i%5==0 and i%3==0):
        New_Num.append(i)
print("List of 3 and 5 Multiplies:   ")
print(New_Num)
