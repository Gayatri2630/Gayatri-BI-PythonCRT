Num1=int(input("Enter the First Value:"))
Num2=int(input("Enter the Second Value:"))
print("Num1=",Num1)
print("Num2=",Num2)
'''
temp=Num1
Num1=Num2
Num2=temp
'''
#Num1,Num2=Num2,Num1
Num1=Num1+Num2
Num2=Num1-Num2
Num1=Num1-Num2
print("After Swapping:")
print("Num1=",Num1)
print("Num2=",Num2)