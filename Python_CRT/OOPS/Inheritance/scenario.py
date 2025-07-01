'''
1.Create a Person class that serves as a base class for both doctors and patients. This class should contain:
*Name
*Age
*Gender
*A method to return formatted personal details.
2.Create a Patient class that inherits from Person and includes:
*Disease information
*A method to return full patient details.
3.Create a Doctor class that iherits from Person and includes:
*Specialization
*A private list to store assigned patients
*Methods to assign a patient, retrieve doctor details and list assigned patients.
4)Implement a "menu-driven interface" that allows the following actions:
1.Add a new doctor
2.Add a new patient
3.Assign a patient to a doctor
4.view all patients assigned to a particular doctor 
5.Search and view details of a specific patient
'''
class Person:
    def __init__(self,Name,Age,Gender):
        self.Name=Name
        self.Age=Age
        self.Gender=Gender
    def get_details(self):
        print(f"Person's Name :{self.Name}")
        print(f"Person's Age : {self.Age}")
        print(f"Person's Gender : {self.Gender}")
class Patient(Person):
    def __init__(self,Name,Age,Gender,Disease):
        super().__init__(Name,Age,Gender)
        self.Disease=Disease
    def get_patient_details(self):
        print(f"Patient's Name :{self.Name}")
        print(f"Patient's Age : {self.Age}")
        print(f"Patient's Gender : {self.Gender}")
        print(f"Disease Description: {self.Disease}")
        #return f"{self.get_details()}, Disease Description: {self.Disease}"
class Doctor(Person):
    def __init__(self,Name,Age,Gender,Specialization):
        super().__init__(Name,Age,Gender)
        self.Specialization=Specialization
        self.__Patients=[]
    def assign_patient(self,patient):
        self.__Patients.append(patient)
    def get_doctor_details(self):
        print(f"Doctor's Name :{self.Name}")
        print(f"Doctor's Age : {self.Age}")
        print(f"Doctor's Gender : {self.Gender}")
        print(f"Doctor's Specialization: {self.Specialization}")
        #return f"{self.get_details()}, Specializatio: {self.Specialization}"
    def get_assigned_patients(self):
        if not self.__Patients:
            return "No Patients Assigned."
        result=""   
        for p in self.__Patients:
            result+=f"-{p.name} ({p.disease})\n" 
        return result.strip()
doctors=[]
patients=[]
def find_doctor_by_name(name):
    for doc in doctors:
        if doc.name.lower()==name.lower():
            return doc
    return None
def find_patient_by_name(name):
    for pat in patients:
        if pat.name.lower()==name.lower():
            return pat
    return None
def main():
    while True:
        print("\n----- Hospital Management System------")
        print("1. Register Doctor")
        print("2. Register Patient")
        print("3. Assign Patient to Doctor")
        print("4. View Doctor and Assigned Patient")
        print("5. View Patient Details")
        print("6. Exit")
        choice=input("Enter your choice:")
        if choice=='1':
            name=input("Doctor Name:")
            age=int(input("Doctor Age:"))
            gender=input("Doctor Gender:")
            Specialization=input("Specialization:")
            doc=Doctor(name,age,gender,Specialization)
            doctors.append(doc)
            print("Doctor registered successfully.")
        elif choice=='2':
            name=input("Patient Name:")
            age=int(input("Doctor Age:"))
            gender=input("Doctor Gender:")
            disease=input("Disease:")
            pat=Patient(name,age,gender,disease)
            patients.append(pat)
            print("Patient registered successfully.")     
        elif choice=='3':
            patient_name=input("Enter Patient Name:")   
            doctor_name=input("Enter Doctor Name:")
            if pat and doc:
                doc.assign_patient(pat)
                print("Patient assigned successfully.")
            else:
                print("Doctor or Patient not found.")
        elif choice=='4':
            doctor_name=input("Enter Doctor Name:")
            doc=find_doctor_by_name(doctor_name)
            if doc:
                print(doc.get_doctor_details())
                print("Assigned Patients:")
                print(doc.get_assigned_patients())
            else:
                print("Doctor not Found.")
        elif choice=='5':
            patient_name=input("Enter Patient Name:")
            pat=find_patient_by_name(patient_name)
            if pat:
                print(pat.get_patient_details())
            else:
                print("Patient not found.")
        elif choice=='6':
            print("Exiting the system.")
            break
        else:
            print("Invalid Choice. Please enter a number between 1 and 6. ")
if __name__=="__main__":
    main()