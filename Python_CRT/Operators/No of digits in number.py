Num=int(input("Enter the Integer Value:"))
temp=Num
digitcount=0
while (Num!=0):
    Num=Num//10
    digitcount+=1
print(f"{temp} has {digitcount} digits")