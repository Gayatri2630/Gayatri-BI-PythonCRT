Str="GAYATRI"
'''
G A Y A T R I 
G A Y A T R I 
G A Y A T R I 
G A Y A T R I 
G A Y A T R I 
G A Y A T R I 
G A Y A T R I 
'''
for i in range(len(Str)):
    for j in range(len(Str)):
        print(f"{Str[j]} ",end="")
    print()
print("--------------------------------------------")
'''
I R T A Y A G 
I R T A Y A G 
I R T A Y A G 
I R T A Y A G
I R T A Y A G
I R T A Y A G
I R T A Y A G
'''
Length=len(Str)
for i in range(Length):
    for j in range(Length):
        print(f"{Str[Length-j-1]} ",end="")
    print()
print("--------------------------------------------")
'''
G
G A
G A Y
G A Y A
G A Y A T
G A Y A T R
G A Y A T R I
'''
for i in range(Length):
    for j in range(i+1):
        print(f"{Str[j]} ",end="")
    print()
print("--------------------------------------------")
'''
G
A A
Y Y Y
A A A A
T T T T T
R R R R R R
I I I I I I I
'''
for i in range(Length):
    for j in range(i+1):
        print(f"{Str[i]} ",end="")
    print()
print("--------------------------------------------")
'''
G A Y A T R I
G           I
G           I
G           I
G           I
G           I
G A Y A T R I
'''
for i in range(Length):
    for j in range(Length):
        if(i==0 or i==Length-1 or j==0 or j==Length-1):
            print(f"{Str[j]} ",end="")
        else:
            print("  ",end="")
    print()
print("--------------------------------------------")
'''   
      G
      A
      Y
G A Y A T R I
      T
      R
      I
'''
for i in range(Length):
    for j in range(Length):
        if i==Length//2:
            print(f"{Str[j]}  ",end=" ")
        elif j==Length//2:
            print(f"{Str[i]}  ",end=" ")
        else:
            print("   ",end=" ")
    print()
print("--------------------------------------------")
'''
      A                 4
    Y A T             3 4 5
  A Y A T R         2 3 4 5 6
G A Y A T R I     1 2 3 4 5 6 7 
  A Y A T R         2 3 4 5 6
    Y A T             3 4 5
      A                 4
'''
for i in range(len(Str)):
    if(i<=len(Str)//2):
        for j in range(len(Str)):
            if(j>=(len(Str)//2)-i and j<=(len(Str)//2)+i):
                print(Str[j],end=" ")
            else:
                print(" ",end=" ")
        print()
    else:
        k=(len(Str))-1-i
        for j in range(len(Str)):
            if(j>=(len(Str)//2)-k and j<=(len(Str)//2)+k):
                print(Str[j],end=" ")
            else:
                print(" ",end=" ")
        print()