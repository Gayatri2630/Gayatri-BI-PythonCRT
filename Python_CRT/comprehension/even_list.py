''' 
Write a python program to print even numbers from 1 to using list comprehension
'''
n=int(input("Enter the number of Values:"))
Num=[i for i in range(n) if i%2==0]
print(Num)