Num=int(input("Enter the intger Value:"))
even_count=0
odd_count=0
while Num!=0:
    rem=Num%10
    if rem%2==0:
        even_count+=1
    else:
        odd_count+=1
    Num//=10
print(f"No of Even digits are {even_count}")
print(f"No of Odd digits are {odd_count}")