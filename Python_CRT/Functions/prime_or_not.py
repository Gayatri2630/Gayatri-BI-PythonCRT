def Prime(Num):
    count=0
    for i in range(2,Num):
        if Num%i==0:
            count+=1
    if count==0:
        print(f"{Num} is Prime Number")
    else:
        print(f"{Num} is not Prime Number")
Prime(2)
Prime(4)
Prime(7)
Prime(10)
Prime(25)

