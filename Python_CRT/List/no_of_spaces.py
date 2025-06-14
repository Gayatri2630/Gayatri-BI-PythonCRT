'''
Write a python program to read the string as input from the user
a) print the string as a list of individual characters
b) find the length of the String
c) find the minimum element after converting string into list
d) find the number of spaces present in the string without using any built-in methods or function
'''
Str=input("Enter a string :")
#prints the list of individual characters in a string
list=[]
len=0
for ch in Str:
    list.append(ch)
print("List of Charcters :",list)
#prints the length of the string
len=0
for ch in Str:
    len+=1
print("Length of the string :",len)
#prints the minimum element
min_char=Str[0]
for ch in Str:
    if ch<min_char:
        min_char=ch
print("Minimumm character in the string :",min_char)
#Count the no.of spaces
spaces=0
for ch in Str:
    if ch==' ':
        spaces+=1
print("Number of Spaces :",spaces)