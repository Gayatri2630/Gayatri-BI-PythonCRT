'''
Write a python program to create a shape class & declare the properties as
Length
Breadth
Height
i)Calculate the Area of Square using instance method
ii)Check Whether the sides of Squares are equal or not using instance method 
iii)Calculate the perimeter of square using instance method
iv)Find the diagonals of Square using instance method
v)Find the Side Length of Square using instance method
'''
class Shape:
    def __init__(self,length,breadth,height):
        self.Length=length
        self.Breadth=breadth
        self.Height=height
    def Set_Area(self):
        area=self.Length*self.Breadth
        self.Area=area
        print(f"Area of Square: {self.Area}")
    def Set_Equal(self):
        if self.Length==self.Breadth:
            print("Equal")
        else:
            print("Not Equal")
    def Set_Perimeter(self):
        perimeter=4*self.Length
        self.Perimeter=perimeter
        print(f"Perimeter of Square:{self.Perimeter}")
    def Set_Length(self):
        print(f"Side Length of Square: {self.Length}")
    def Set_Diagonal(self):
        diagonal=pow(2,1/2)*self.Length
        self.Diagonal=diagonal
        print(f"Diagonal of Square: {self.Diagonal:.1f}")
        
S1=Shape(4,4,6)
S1.Set_Area()
S1.Set_Equal()
S1.Set_Perimeter()
S1.Set_Length()
S1.Set_Diagonal()

    