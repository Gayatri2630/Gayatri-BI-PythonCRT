def Tables(n):
    for i in range(1,n+1):
        print(f"Mutliplication Table of {i}:")
        for j in range(1,11):
            print(f"{i}x{j}={i*j}")
Tables(5)