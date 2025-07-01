class Employee:
    def __init__(self,empname,empID,designation,salary,deptname):
        print("Object is Created")
        self.EmpName=empname
        self.EmpID=empID
        self.Designation=designation
        self.Salary=salary
        self.DeptName=deptname
def Display_details(self):
    print(f"Employee Name:{E1.EmpName}")
    print(f"Employee ID:{E1.EmpID}")
    print(f"Employee's Designation:{E1.Designation}")
    print(f"Employee's Salary:{E1.Salary}")
    print(f"Employee's DeptName:{E1.DeptName}")
E1=Employee("Scott","EMP101",'Data Analyst',25000,'DeploymentTeam')
Display_details(E1)
E2=Employee("Gayatri","EMP102",'Data Engineer',26000,'DeploymentTeam')
Display_details(E2)
E3=Employee("Nazma","EMP103",'Full Stack Development',30000,'DeploymentTeam')
Display_details(E3)
E4=Employee("Joy","EMP104",'Data scientist',35000,'DeploymentTeam')
Display_details(E4)
E5=Employee("Bhargavi","EMP105",'Java Developer',40000,'DeploymentTeam')
Display_details(E5)
