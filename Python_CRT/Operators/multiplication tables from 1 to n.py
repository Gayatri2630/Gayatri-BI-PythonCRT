Num=int(input("Enter the Integer Value:"))
for i in  range(Num+1):
    print(f"Multiplication Table of {i}:")
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
