Num=int(input("Enter the Intger Value:"))
#using if-else
if Num>=100 and Num<=999:
    print(f"{Num} is a Three-digit Number")
else:
    print(f"{Num} is not a Three-digit Number")
#using ternary operator
Result="a Three-digit Number" if Num>=100 and Num<=999 else "not a Three-digit Number"
print(f"{Num} is {Result}")