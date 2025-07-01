'''
write a python program to read month number from user and check whether i is valid number or not.
'''
Month=int(input("Enter the Month Number:"))
if(Month>=1 and Month<=12):
    print("Valid Month Number")
else:
    print("In-Valid Month NUmber")