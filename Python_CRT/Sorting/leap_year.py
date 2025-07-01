'''
write a python program to read a year as input from user and check whether it is leap or not.
'''
year=int(input("Enter the year:"))
if (year%4==0 and year%100!=0 or year%400==0):
    print("Leap year")
else:
    print("Not a Leap Year")