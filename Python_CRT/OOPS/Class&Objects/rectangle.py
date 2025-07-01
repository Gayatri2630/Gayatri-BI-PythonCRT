'''
Write a python program to create a rectangle class and initialize the variables length and breadth using contructor and acess the values
using mutator methods
'''
class Rectangle:
    def __init__(self,length,breadth):
        self.Length=length
        self.Breadth=breadth
    def Set_Details(self):
        print(f"Length of Rectangle : {self.Length}")
        print(f"Breadth of Rectangle : {self.Breadth}")
R1=Rectangle(5,6)
R1.Set_Details()
print("------------------")
R2=Rectangle(17,19)
R2.Set_Details()

