#creating list to enter the elements from the user
size=int(input("Enter the Size of List:"))
prog_lang=[]
#reading the list elements as input
for i in range(size):
    Temp=input("Enter the Elements:")
    prog_lang.append(Temp)
print("Elements of the List:")
print(prog_lang)