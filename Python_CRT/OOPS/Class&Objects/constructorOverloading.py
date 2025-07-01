'''
Write a Python program to create a employee class and declare the states and create 5 object using different constructors
'''
class Employee:
    def __init__(self,EmpName,EmpID,Job,Salary,Location,Dept):
        self.EmpName=EmpName
        self.EmpID=EmpID
        self.Job=Job
        self.Salary=Salary
        self.Location=Location
        self.Dept=Dept
        print("Hey..! I'm a Six Parameterized Constructor")
    def __init__(self,EmpName,EmpID,Job,Salary,Location):
        self.EmpName=EmpName
        self.EmpID=EmpID
        self.Job=Job
        self.Salary=Salary
        self.Location=Location
        print("Hey..! I'm a Five Parameterized Constructor")
    def __init__(self,EmpName,EmpID,Job,Salary):
        self.EmpName=EmpName
        self.EmpID=EmpID
        self.Job=Job
        self.Salary=Salary
        print("Hey..! I'm a Four Parameterized Constructor")
    def __init__(self,EmpName,EmpID,Job):
        self.EmpName=EmpName
        self.EmpID=EmpID
        self.Job=Job
        print("Hey..! I'm a Three Parameterized Constructor")
    def __init__(self,EmpName,EmpID):
        self.EmpName=EmpName
        self.EmpID=EmpID
        print("Hey..! I'm a Two Parameterized Constructor")
    def __init__(self,EmpName):
        self.EmpName=EmpName
        print("Hey..! I'm a One Parameterized Constructor")
    def __init(self):
        print("Hey..! I'm a Zero Parameterized Constructor")

Emp1=Employee()
Emp2=Employee("Gayatri")
Emp3=Employee("Gayatri",101)
Emp4=Employee("Sahithi",102,'HR')
Emp5=Employee("Anusha",103,'Developer',25000)
Emp6=Employee("Gopaali",104,'Data Analyst',30000,'Bengaluru')
