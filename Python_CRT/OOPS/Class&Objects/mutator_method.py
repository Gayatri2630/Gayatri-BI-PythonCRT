#Mutator method->
class Mobile:
    def __init__(self,P,C,B):
        self.Price=P
        self.Color=C
        self.Brand=B
        print("Object is Created")
    def Set_Color(self):
        self.Color='Blue'
    def Get_details(self):
        print(f"Color : {self.Color}")
        print(f"Price : {self.Price}")
        print(f"Brand : {self.Brand}")
M1=Mobile(12000,"Black","Samsung")
M1.Get_details()
print("After Modification:")
M1.Set_Color()
M1.Get_details()
M2=Mobile(14000,"Grey","Vivo")
M2.Get_details()
print("After Modification:")
M2.Set_Color()
M2.Get_details()
M3=Mobile(16000,"Cream","Oppo")
M3.Get_details()
print("After Modification:")
M3.Set_Color()
M3.Get_details()
M4=Mobile(20000,"White","One Plus")
M4.Get_details()
print("After Modification:")
M4.Set_Color()
M4.Get_details()
M5=Mobile(22000,"Purple","")
M5.Get_details()
print("After Modification:")
M5.Set_Color()
M5.Get_details()
