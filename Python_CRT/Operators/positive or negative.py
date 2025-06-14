Num=int(input("Enter the Integer Value: "))
#using if-else
if(Num>0):
    print(f"{Num} is +ve Number")
elif(Num<0):
    print(f"{Num} is -ve Number")
else:
    print(f"{Num} is 0")
#using ternary operator
Res="+ve Number" if(Num>0) else "-ve Number"
print(f"{Num} is {Res}")