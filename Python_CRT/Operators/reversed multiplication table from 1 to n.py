Num=int(input("Enter the value of Num:"))
for i in range(Num+1):
    print(f"Multiplication Table of {i}:")
    for j in range(10,0,-1):
        print(f"{i}x{j}={j*i}")