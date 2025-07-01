'''
Write a python program to create a product class and declare the states of the class as product name,product id,price,gst,
manfacture date and expiry date and create five objects intialize it with parameterized constructor and access the elements using the 
instance method and declare the mutator method as for all 6 properties and change their values of properties using mutator methos and 
print it
'''
class Product:
    def __init__(self,name,productID,price,gst,manufacturedata,expirydate):
        self.ProductName=name
        self.ProductID=productID
        self.Price=price
        self.GST=gst
        self.ManufactureDate=manufacturedata
        self.ExpiryDate=expirydate
        print("Product is Created")
    def Set_Product(self):
        self.ProductName='Biscuit'
        self.ProductID='23456'
        self.Price=40
        self.GST=12
        self.ManufactureDate='22-10-2025'
        self.ExpiryDate='23-4-2026'
    def Get_details(self):
        print(f"Product Name : {self.ProductName}")
        print(f"Product ID : {self.ProductID}")
        print(f"Price : {self.Price}")
        print(f"GST : {self.GST}")
        print(f"Manfacture Date : {self.ManufactureDate}")
        print(f"Expiry Date : {self.ExpiryDate}")
P1=Product("Popins","1245",30,15,"21-03-2024","22-08-2024")
P1.Get_details()
print("After Modification:")
P1.Set_Product()
P1.Get_details()
P2=Product("Lays","1212",10,4,"21-03-2022","22-08-2022")
P2.Get_details()
print("After Modification:")
P2.Set_Product()
P2.Get_details()
P3=Product("Pipper Mints","1543",10,5,"24-04-2024","23-09-2024")
P3.Get_details()
print("After Modification:")
P3.Set_Product()
P3.Get_details()
P4=Product("Chips","6547",20,10,"21-03-2014","22-08-2014")
P4.Get_details()
print("After Modification:")
P4.Set_Product()
P4.Get_details()
P5=Product("Polo","4356",10,6,"20-03-2023","21-08-2023")
P5.Get_details()
print("After Modification:")
P5.Set_Product()
P5.Get_details()
