Num=int(input("Enter the Integer Value:"))
digitsum=0
while(Num!=0):
    Rem=Num%10
    digitsum=digitsum+Rem
    Num=Num//10
print(f"Summation is {digitsum}")
