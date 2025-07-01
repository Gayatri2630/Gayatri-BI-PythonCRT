'''
write a python program to write a lambda function which prints good students if branch is bioinformatics else bad students
'''
name=lambda x:print("Good Students") if(x=="Bioinformatics") else print("Bad Students")
name("Bioinformatics")
name("CSE")