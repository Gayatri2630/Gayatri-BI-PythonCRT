Size=int(input("Enter the length of list:"))
Char_List=[]
for i in range(Size):
    ch=input("Enter the characters:")
    Char_List.append(ch)
print(Char_List)
str="".join(Char_List)
print(str)