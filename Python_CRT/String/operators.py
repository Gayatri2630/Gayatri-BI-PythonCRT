#length of string
Str="python"
print(f"Length of {Str} is {len(Str)}")
#Accessing without index
for i in Str:
    print(i,end=" ")
print()
#Accessing without index
for i in range(len(Str)):
    print(Str[i],end=" ")
print()
#type  error because strings are immutable
str1="Students"
str1[4]="i"
for c in str1:
    print(c)
