'''
Write a python program to create a student class and declare the properties as student name,student id,branch,percentage,age,year of 
pass out and no.of certfications has and create 10 objects and intialize the values using mutator method and access the values using 
accessor method. (Note:intialize values without constructor)
'''
class Student:
    StudentName=input("Enter the Name of the Student:")
    def Set_StudentName(self):
        self.StudentName='Bhoomi'
        print(f"{self.StudentName}")
    StudentID=input("Enter the Student ID:")
    def Set_StudentID(self):
        self.StudentID='221fa1345'
        print(f"{self.StudentID}")
    Branch=input("Enter the Branch:")
    def Set_Branch(self):
        self.Branch='BI'
        print(f"{self.Branch}")
    Percentage=int(input("Enter the Percentage:"))
    def Set_Percentage(self):
        self.Percentage='70%'
        print(f"{self.Percentage}")
    Age=int(input("Enter the Age:"))
    def Set_Age(self):
        self.Age=20
        print(f"{self.Age}")
    YearPassing=int(input("Enter the Year of Passing:"))
    def Set_YearPassing(self):
        self.YearPassing='2026'
        print(f"{self.YearPassing}")
    Certificates=int(input("Enter the Number of Certifcates:"))
    def Set_Certificates(self):
        self.Certificates=15
        print(f"{self.Certificates}")
S1=Student()
print("After Modification:")
S1.Set_StudentName()
S1.Set_StudentID()
S1.Set_Branch()
S1.Set_Percentage()
S1.Set_Age()
S1.Set_Certificates()

