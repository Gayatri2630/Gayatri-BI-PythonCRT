#natural numbers from 1 to n
Num=int(input("Enter the Value of Num:"))
print(f"Natural Numbers from 1 to {Num}:")
for i in range(1,Num+1):
    print(i,end=" ")
print()
#natural numbers from n to 1
print(f"Natural Numbers from {Num} to 1:")
for i in range(Num,0,-1):
    print(i,end=" ")
