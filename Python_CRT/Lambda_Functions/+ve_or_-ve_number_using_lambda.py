'''
write a python program to check whether the number is positive or negative using lambda functions
'''
num=lambda n:print("Positive") if(n>0)  else(print("Zero")) if (n==0) else print("Negative")
# using user defined function
def Positive(Num):
    if(Num>0):
        print("Positive")
    else:
        if(Num==0):
            print("Zero")
        else:
            print("Negative")
num(-9)
num(0)
num(5)
Positive(0)
