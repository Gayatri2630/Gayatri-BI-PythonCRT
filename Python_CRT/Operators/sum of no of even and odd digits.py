Num=int(input("Enter the intger Value:"))
even_sum=0
odd_sum=0
while Num!=0:
    rem=Num%10
    if rem%2==0:
        even_sum+=rem
    else:
        odd_sum+=rem
    Num//=10
print(f"Sum of Even digits are {even_sum}")
print(f"Sum of Odd digits are {odd_sum}")