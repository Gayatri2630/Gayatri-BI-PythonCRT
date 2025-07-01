#Time Complexity=O(n^2)->worst complexity
Arr=[25,15,10,20,5]
print(f"Original Array : {Arr}")
for i in range(len(Arr)):
    Flag=False
    for j in range(len(Arr)-1):
        if (Arr[j]>Arr[j+1]):
            Arr[j],Arr[j+1]=Arr[j+1],Arr[j]
            print(Arr)
            Flag=True
    if Flag==False:
        break
print(Arr)