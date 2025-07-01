'''
Write a python program to create a Book Class declare the states as
BookName
AuthorName
PublisherName
PublisherDate
Categroy of Book
i)Create 5 objects &intialize the values using constructor where out of five
   -- Create 1st Object using one parameterized constructor
   --Create 2nd  Object using two parameters constructor
   --Create 3rd Object using zero parameterized constructor
   --Create 4th Object using four parameterized constructor
   --Create 5th Object using five parameterized constructor
ii)Access the Values using accessor methods
iii)Update the Values using Mutator Method for Name of the book
'''
class Book1:
   def __init__(self,name):
      self.Name=name
   def Set_BookName(self):
      self.Name='Python'
   def Get_Details(self):
      print(f"Book Name : {self.Name}")
class Book2:
   def __init__(self,name,authorname):
      self.Name=name
      self.AuthorName=authorname
   def Set_BookName(self):
      self.Name='Python'
   def Get_Details(self):
      print(f"Book Name : {self.Name}")
      print(f"Author Name : {self.AuthorName}")
class Book3:
   def __init__(self):
      print("Object is Created")
class Book4:
   def __init__(self,name,authorname,publishername,publisherdate):
      self.Name=name
      self.AuthorName=authorname
      self.PublisherName=publishername
      self.PublisherDate=publisherdate
   def Set_BookName(self):
      self.Name='Python'
   def Get_Details(self):
      print(f"Book Name : {self.Name}")
      print(f"Author Name : {self.AuthorName}")
      print(f"Publisher Name : {self.PublisherName}")
      print(f"Publisher Date : {self.PublisherDate}")     
class Book5:
   def __init__(self,name,authorname,publishername,publisherdate,categoryofbook):
      self.Name=name
      self.AuthorName=authorname
      self.PublisherName=publishername
      self.PublisherDate=publisherdate
      self.CategroyofBook=categoryofbook
   def Set_BookName(self):
      self.Name='Python'
   def Get_Details(self):
      print(f"Book Name : {self.Name}")
      print(f"Author Name : {self.AuthorName}")
      print(f"Publisher Name : {self.PublisherName}")
      print(f"Publisher Date : {self.PublisherDate}")
      print(f"Category Of Book : {self.CategroyofBook}")
B1=Book1("Java")
B1.Set_BookName()
B1.Get_Details()
print("---------------------------")
B2=Book2("Java","R.D.Sharma")
B2.Set_BookName()
B2.Get_Details()
print("---------------------------")
B3=Book3()
print("---------------------------")
B4=Book4("Java","R.D.Sharma","Mukesh","22-10-1004")
B4.Set_BookName()
B4.Get_Details()
print("---------------------------")
B5=Book5("Java","R.D.Sharma","Mukesh","22-10-1004","Education")
B5.Set_BookName()
B5.Get_Details()
